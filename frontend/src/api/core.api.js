import api from "./config.js"

export default {
  async getEmail () {
    const response = await api.get("/api/core/email/list")
    return response.data
  },
  async addNewEmai (description) {
    const json = JSON.stringify({ description })
    const response = await api.post(
      "/api/core/email/add",
      json
    )
    return response.data
  },
  async sendChatMessage(message){
    const json = {message}
    const response = await api.post(
      "/api/core/chat",
      json
    )
    return response.data
  }
}
