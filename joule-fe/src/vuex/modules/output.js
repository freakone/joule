import {
  GET_OUTPUTS
} from '../mutation-types'

const state = {
  items: [
    {
      id: 1,
      value: true,
      name: 'pompa1'
    },
    {
      id: 2,
      value: true,
      name: 'pompa góra'
    },
    {
      id: 3,
      value: false,
      name: 'pompa3'
    }
  ]
}

// mutations
const mutations = {
  [GET_OUTPUTS] (state, items) {
    state.items.push(items)
  }
}

export default {
  state,
  mutations
}
