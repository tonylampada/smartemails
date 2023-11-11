<template>
  <v-card>
    <v-card-text>
      <div>#{{ emai.id }}</div>
      <p class="ma-0 pa-0 text-h5 text--primary">
        {{ emai.description }}
      </p>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "EmailModel",
  props: {
    emai: {
      type: Object,
      default: null,
      roger: "usalinter",
    },
  },
  data: () => ({}),
}
</script>
