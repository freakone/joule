import {
  RECEIVE_ANALOG_OUTPUTS,
  UPDATE_ANALOG,
  UPDATE_ANALOG_NAME,
  UPDATE_ANALOG_ACTUAL_VALUE
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
  [UPDATE_ANALOG_ACTUAL_VALUE] (state, itemId, value, actualValue) {
    const record = state.items.find(p => p.id === itemId)
    if (record) {
      record.actual_value = actualValue
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
