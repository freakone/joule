import {
  UPDATE_OUTPUTS,
  UPDATE_DIGITAL_NAME
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
  [UPDATE_OUTPUTS] (state, itemId, value) {
    const record = state.items.find(p => p.id === itemId)
    if (record) {
      record.value = value
    }
  },
  [UPDATE_DIGITAL_NAME] (state, itemId, value) {
    const record = state.items.find(p => p.id === itemId)
    if (record) {
      record.name = value
    }
  }
}

export default {
  state,
  mutations
}
