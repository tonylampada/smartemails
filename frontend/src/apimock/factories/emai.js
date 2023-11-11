import { Factory } from "miragejs"
import { faker } from "@faker-js/faker"

export const emai = Factory.extend({
  description() {
    return faker.word.verb()
  },
})
