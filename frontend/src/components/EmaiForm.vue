<template>
  <div>
    <v-card>
      <v-card-text>
        <v-text-field
          v-model="title"
          :label="formLabel"
          required
          outlined
          append-icon="fa-pen"
          @keyup.enter="addNewEmai" />
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  props: {
    formLabel: {
      type: String,
      default: "",
    },
  },
  emits: ["newEmai"],
  data: () => {
    return {
      title: "",
    }
  },
  methods: {
    addNewEmai() {
      this.$emit("newEmai", {
        title: this.title,
      })
      this.title = ""
    },
  },
}
</script>

<style scoped></style>
