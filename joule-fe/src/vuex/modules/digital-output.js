import {
  UPDATE_OUTPUT,
  UPDATE_DIGITAL_NAME,
  RECEIVE_DIGITAL_OUTPUTS
} from '../mutation-types'

const state = {
  items: []
}

const mutations = {
  [UPDATE_OUTPUT] (state, itemId, value) {
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
  },
  [RECEIVE_DIGITAL_OUTPUTS] (state, items) {
    state.items = items
  }
}

export default {
  state,
  mutations
}
