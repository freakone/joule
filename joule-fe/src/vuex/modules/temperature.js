import {
  ADD_TEMPERATURE,
  SELECT_TEMPERATURE,
  UPDATE_TEMPERATURE_NAME,
  UPDATE_TEMPERATURE_MINIMUM,
  UPDATE_TEMPERATURE_MAXIMUM,
  RECEIVE_TEMPERATURE_INPUTS
} from '../mutation-types'

const state = {
  items: [],
  selectedSensor: {}
}

const mutations = {
  [RECEIVE_TEMPERATURE_INPUTS] (state, items) {
    state.items = items
  },
  [ADD_TEMPERATURE] (state, itemId, value) {
    const record = state.items.find(p => p.id === itemId)
    if (record) {
      record.datasets.data.push(value)
    }
  },
  [SELECT_TEMPERATURE] (state, itemId) {
    state.selectedSensor = state.items.find(p => p.id === itemId)
  },
  [UPDATE_TEMPERATURE_NAME] (state, itemId, value) {
    const record = state.items.find(p => p.id === itemId)
    if (record) {
      record.name = value
    }
  },
  [UPDATE_TEMPERATURE_MINIMUM] (state, itemId, value) {
    const record = state.items.find(p => p.id === itemId)
    if (record) {
      record.limitMin = value
    }
  },
  [UPDATE_TEMPERATURE_MAXIMUM] (state, itemId, value) {
    const record = state.items.find(p => p.id === itemId)
    if (record) {
      record.limitMax = value
    }
  }
}

export default {
  state,
  mutations
}
