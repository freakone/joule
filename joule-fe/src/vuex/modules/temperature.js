import {
  ADD_TEMPERATURES,
  SELECT_TEMPERATURE,
  UPDATE_TEMPERATURE_NAME,
  UPDATE_TEMPERATURE_MINIMUM,
  UPDATE_TEMPERATURE_MAXIMUM
} from '../mutation-types'

// const initDataset = [{
//   backgroundColor: 'rgba(220,220,220,0.9)',
//   borderColor: 'rgba(220,220,220,1)',
//   borderWidth: 1,
//   hoverBackgroundColor: 'rgba(220,220,220,0.5)',
//   hoverBorderColor: 'rgba(220,220,220,1)',
//   data: [],
//   yAxisID: 'y-axis-0'
// }]

const state = {
  items: [
    {
      id: 1,
      name: 'temp1',
      currentValue: 25,
      limitMin: 4,
      limitMax: 30,
      labels: [],
      options: {},
      datasets: []
    },
    {
      id: 2,
      name: 'temp 55',
      currentValue: 230,
      limitMin: 200,
      limitMax: 300,
      labels: ['1', '2', 'as', 'asd', 'asd'],
      options: {},
      datasets: [{ data: [1, 2, 3, 4, 5] }]
    }
  ],
  selectedSensor: {}
}

// mutations
const mutations = {
  [ADD_TEMPERATURES] (state, itemId, value) {
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
