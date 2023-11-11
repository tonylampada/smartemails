<template>
  <div class="chat-container">
    <div class="chat-messages">
      <div
        v-for="(message, index) in messages"
        :key="index"
        class="message"
        :class="{ sender: message.sender === 'user', receiver: message.sender === 'agent' }">
        <span>{{ message.text }}</span>
      </div>
    </div>
    <div class="chat-input">
      <VTextField
        placeholder="Type a message..."
        solo-inverted
        flat
        hide-details
        :disabled="isSending"
        :loading="isSending"
        @keyup.enter="onEnter"
        v-model="message"></VTextField>
    </div>
  </div>
</template>

<script>
import coreApi from "@/api/core.api.js"

export default {
  name: "ChatComponent",
  data() {
    return {
      message: "",
      isSending: false,
      messages: [
        { text: "Hello, how can I assist you?", sender: "agent" },
        { text: "I need help with my order.", sender: "user" },
        { text: "Sure, I can help with that.", sender: "agent" },
        // More hardcoded messages
      ],
    }
  },
  methods: {
    async onEnter() {
      this.isSending = true
      const message = this.message
      this.messages.push({ text: message, sender: "user" })
      this.message = ""
      const result = await coreApi.sendChatMessage(message)
      result.message = result.message || "ok"
      this.messages.push({ text: result.message, sender: "agent" })
      if (result.action) {
        this.$emit("action", result.action)
      }
      this.isSending = false
    },
  },
}
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  background-color: white;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 10px;
  display: flex;
  flex-direction: column;
}

.message {
  margin: 5px;
  padding: 10px;
  border-radius: 10px;
  max-width: 70%;
  display: flex;
}

.sender {
  background-color: #e0f7fa;
  margin-left: auto; /* Pushes user messages to the right */
}

.receiver {
  background-color: #eceff1;
  margin-right: auto; /* Keeps agent messages on the left */
}

.chat-input {
  margin: 10px;
}
</style>
