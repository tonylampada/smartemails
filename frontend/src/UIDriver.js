import EventBus from "./EventBus.js"
import router from "./router/index.js";
import {nextTick} from "vue"

const UIDriver = {
  showEmails() {
    router.push({ name: 'email-list' });
  },
  async composeEmail({ recipient, subject, body }) {
    await router.push({ name: 'email-compose' });
    console.log("set route")
    EventBus.emit('compose-email', { recipient, subject, body });
    console.log("emmited event")
  }
}

export default UIDriver;
