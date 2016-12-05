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

var dateFormat = require('dateformat')

const mutations = {
  [RECEIVE_TEMPERATURE_INPUTS] (state, items) {
    state.items = items
  },
  [ADD_TEMPERATURE] (state, itemId, value) {
    const record = state.items.find(p => p.id === itemId)
    if (record) {
      var newDataset = record.datasets.slice()
      if (newDataset[0].data.length > 60) {
        record.labels = record.labels.slice(-61)
        newDataset[0].data = newDataset[0].data.slice(-60)
      }

      var label = dateFormat(Date.now(), 'HH:MM:ss')
      record.labels.push(label)
      newDataset[0].data.push(value)
      record.datasets = newDataset
      record.currentValue = value
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
