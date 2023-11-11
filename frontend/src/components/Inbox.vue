<template>
  <div class="inbox-container">
    <v-list dense>
      <v-list-item v-for="(email, index) in emails" :key="index">
        <v-list-item-content>
          <v-list-item-title>{{ email.subject }}</v-list-item-title>
          <v-list-item-subtitle>{{ email.sender }} - {{ email.date }}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <v-btn color="primary" :to="{ name: 'email-compose' }">Compose</v-btn>
  </div>
</template>

<script>
export default {
  name: "InboxComponent",
  data() {
    return {
      emails: [
        { sender: "John Doe", subject: "Meeting Schedule", date: "2023-11-01" },
        { sender: "Jane Smith", subject: "Project Update", date: "2023-11-02" },
        { sender: "Acme Corp", subject: "Invoice Details", date: "2023-11-03" },
        // Add more fake email data here
      ],
    }
  },
  methods: {
    composeEmail() {
      // Placeholder for compose action
      alert("Compose new email")
    },
  },
}
</script>

<style scoped>
.inbox-container {
  max-width: 600px;
  margin: auto;
}

.v-list-item:nth-child(odd) {
  background-color: #f5f5f5; /* Light gray for odd items */
}

.v-list-item:nth-child(even) {
  background-color: #ffffff; /* White for even items */
}

.v-btn {
  margin: 20px 0;
}
</style>
