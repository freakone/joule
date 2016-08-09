import {
  RECEIVE_MOTORS,
  UPDATE_MOTORS,
  UPDATE_MOTORS_STARTING
} from '../mutation-types'

const state = {
  items: []
}

const mutations = {
  [UPDATE_MOTORS] (state, itemId, value) {
    const record = state.items.find(p => p.id === itemId)
    if (record) {
      record.value = value
    }
  },
  [UPDATE_MOTORS_STARTING] (state, itemId, starting) {
    const record = state.items.find(p => p.id === itemId)
    if (record) {
      record.starting = starting
    }
  },
  [RECEIVE_MOTORS] (state, items) {
    state.items = items
  }
}

export default {
  state,
  mutations
}
