import {
  UPDATE_DIGITAL_INPUT,
  UPDATE_DIGITAL_INPUT_NAME,
  RECEIVE_DIGITAL_INPUTS
} from '../mutation-types'

const state = {
  items: []
}

const mutations = {
  [UPDATE_DIGITAL_INPUT] (state, itemId, value) {
    const record = state.items.find(p => p.id === itemId)
    if (record) {
      record.value = value
    }
  },
  [UPDATE_DIGITAL_INPUT_NAME] (state, itemId, value) {
    const record = state.items.find(p => p.id === itemId)
    if (record) {
      record.name = value
    }
  },
  [RECEIVE_DIGITAL_INPUTS] (state, items) {
    state.items = items
  }
}

export default {
  state,
  mutations
}
