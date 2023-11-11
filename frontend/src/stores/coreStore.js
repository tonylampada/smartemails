import { defineStore } from "pinia"
import coreApi from "@/api/core.api.js"

export const usecoreStore = defineStore("coreStore", {
  state: () => ({
    email: [],
    emailLoading: false,
  }),
  actions: {
    async getEmail() {
      this.emailLoading = true
      const response = await coreApi.getEmail()
      this.email = response.email
      this.emailLoading = false
    },
    async addNewEmai(tarefa) {
      const newEmai = await coreApi.addNewEmai(tarefa.title)
      return newEmai
    },
  },
})
