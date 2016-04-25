import {
  GET_ANALOG,
  UPDATE_ANALOG
} from '../mutation-types'

const state = {
  items: [{
    id: 1,
    value: '25%',
    name: 'test1'
  },
    {
      id: 2,
      value: '25%',
      name: 'test asdf'
    }]
}

// mutations
const mutations = {
  [UPDATE_ANALOG] (state, itemId, value) {
    const record = state.added.find(p => p.id === itemId)
    if (record) {
      record.value = value
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
