import { accounts } from "./accounts"
import { core } from "./core"

export const routes = function () {
  accounts(this), core(this)
}
