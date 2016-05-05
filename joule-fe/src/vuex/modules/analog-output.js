import {
  RECEIVE_ANALOG_OUTPUTS,
  UPDATE_ANALOG,
  UPDATE_ANALOG_NAME
} from '../mutation-types'

const state = {
  items: []
}

const mutations = {
  [UPDATE_ANALOG] (state, itemId, value) {
    const record = state.items.find(p => p.id === itemId)
    if (record) {
      record.value = value
    }
  },
  [UPDATE_ANALOG_NAME] (state, itemId, value) {
    const record = state.items.find(p => p.id === itemId)
    if (record) {
      record.name = value
    }
  },
  [RECEIVE_ANALOG_OUTPUTS] (state, items) {
    state.items = items
  }
}

export default {
  state,
  mutations
}
