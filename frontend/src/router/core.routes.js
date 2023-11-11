// Composables
import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import EmaiListView from "@/views/core/EmaiListView.vue"
import Inbox from "@/components/Inbox.vue"
import Compose from "@/components/Compose.vue"

export default [
  {
    path: "/email",
    component: DefaultLayout,
    children: [
      {
        path: "list",
        name: "email-list",
        component: Inbox,
      },
      {
        path: "compose",
        name: "email-compose",
        component: Compose,
      }
    ],
  }
]
