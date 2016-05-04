import {
  GET_ANALOG,
  UPDATE_ANALOG,
  UPDATE_ANALOG_NAME
} from '../mutation-types'

const state = {
  items: [
    {
      id: 1,
      value: 25,
      name: 'test1'
    },
    {
      id: 2,
      value: 60,
      name: 'test asdf'
    }]
}

// mutations
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
  [GET_ANALOG] (state, items) {
    state.items.push(items)
  }
}

export default {
  state,
  mutations
}
