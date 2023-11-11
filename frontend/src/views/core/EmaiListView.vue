<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12">
        <v-card>
          <v-card-title class="headline"> Email </v-card-title>
        </v-card>
      </v-col>

      <v-col cols="12">
        <emai-form :form-label="'New Emai'" @new-emai="addNewEmai" />
      </v-col>

      <v-col v-for="item in email" :key="item.id" cols="12">
        <emai :emai="item" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from "pinia"
import { useBaseStore } from "@/stores/baseStore"
import { usecoreStore } from "@/stores/coreStore"
import Emai from "@/components/Emai.vue"
import EmaiForm from "@/components/EmaiForm.vue"

export default {
  name: "EmailList",
  components: { Emai, EmaiForm },
  setup() {
    const baseStore = useBaseStore()
    const coreStore = usecoreStore()
    return { baseStore, coreStore }
  },
  computed: {
    ...mapState(usecoreStore, ["email", "emailLoading"]),
  },
  mounted() {
    this.getEmail()
  },
  methods: {
    getEmail() {
      this.coreStore.getEmail()
    },
    async addNewEmai(emai) {
      const newEmai = await this.coreStore.addNewEmai(emai)
      this.baseStore.showSnackbar(`New emai added #${ newEmai.id }`)
      this.getEmail()
    },
  },
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
</style>
