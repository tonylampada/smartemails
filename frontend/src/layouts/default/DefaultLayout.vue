<template>
  <VLayout>
    <app-error-dialog :show="showErrorMessage" :message="errorMessage" @close="closeErrorDialog" />
    <app-snackbar />
    <VApp :theme="theme">
      <app-nav-bar
        :theme="theme"
        @theme-click="onThemeClick"
        @toggle-right-drawer="toggleRightDrawer"></app-nav-bar>
      <VMain>
        <RouterView />
      </VMain>
      <VNavigationDrawer v-model="rightDrawer" right absolute temporary>
        <Chat @action="execChatAction" />
      </VNavigationDrawer>
      <app-footer :fixed="true" :user="loggedUser" />
      <v-btn
        fab
        bottom
        right
        color="primary"
        @click="toggleRightDrawer"
        style="position: fixed; bottom: 90px; right: 16px">
        <VIcon>mdi-message</VIcon>
      </v-btn>
    </VApp>
  </VLayout>
</template>

<script setup>
import { ref } from "vue"
import UIDriver from "@/UIDriver.js"
import EventBus from "@/EventBus.js"

const theme = ref("dark")
const rightDrawer = ref(false)

function onThemeClick() {
  theme.value = theme.value === "light" ? "dark" : "light"
}

function toggleRightDrawer() {
  rightDrawer.value = !rightDrawer.value
}
</script>

<script>
import { mapState } from "pinia"
import { useBaseStore } from "@/stores/baseStore"
import { useAccountsStore } from "@/stores/accountsStore"
import AppSnackbar from "@/components/AppSnackbar.vue"
import AppErrorDialog from "@/components/AppErrorDialog.vue"
import AppNavBar from "@/components/AppNavBar.vue"
import AppFooter from "@/components/AppFooter.vue"
import Chat from "@/components/Chat.vue"

export default {
  name: "DefaultLayout",
  components: {
    AppSnackbar,
    AppErrorDialog,
    AppNavBar,
    AppFooter,
  },
  setup() {
    const baseStore = useBaseStore()
    return { baseStore }
  },
  computed: {
    ...mapState(useBaseStore, ["errorMessage", "showErrorMessage"]),
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
  methods: {
    closeErrorDialog() {
      this.baseStore.setShowErrorMessage(null)
    },
    execChatAction(action) {
      UIDriver[action.operation](action.params || {})
    },
  },
  mounted() {
    window.UIDriver = UIDriver
    window.EventBus = EventBus
  },
}
</script>
