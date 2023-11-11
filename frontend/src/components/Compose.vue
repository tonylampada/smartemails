<template>
  <div class="compose-container">
    <VCard>
      <VCardTitle>Compose Email</VCardTitle>
      <VCardText>
        <VForm ref="form" v-model="valid">
          <VTextField label="To" v-model="email.to" :rules="emailRules" required></VTextField>
          <VTextField
            label="Subject"
            v-model="email.subject"
            :rules="subjectRules"
            required></VTextField>
          <VTextarea
            label="Message"
            v-model="email.message"
            rows="4"
            :rules="messageRules"
            required></VTextarea>
        </VForm>
      </VCardText>
      <VCardActions>
        <VSpacer></VSpacer>
        <VBtn color="primary" @click="sendEmail" :disabled="!valid">Send</VBtn>
      </VCardActions>
    </VCard>
  </div>
</template>

<script>
import EventBus from "@/EventBus.js"
export default {
  name: "ComposeComponent",
  data() {
    return {
      valid: false,
      email: {
        to: "",
        subject: "",
        message: "",
      },
      emailRules: [
        (v) => !!v || "To field is required",
        (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
      ],
      subjectRules: [(v) => !!v || "Subject is required"],
      messageRules: [(v) => !!v || "Message is required"],
    }
  },
  methods: {
    sendEmail() {
      if (this.$refs.form.validate()) {
        // Placeholder for email sending logic
        alert(`Email sent to: ${this.email.to}`)
      }
    },
    prefillForm({ recipient, subject, body }) {
      this.email.to = recipient || ""
      this.email.subject = subject || ""
      this.email.message = body || ""
    },
  },
  created() {
    console.log("set listener")
    EventBus.on("compose-email", this.prefillForm)
  },
  beforeUnmount() {
    EventBus.off("compose-email", this.prefillForm)
  },
}
</script>

<style scoped>
.compose-container {
  max-width: 600px;
  margin: auto;
}
</style>
