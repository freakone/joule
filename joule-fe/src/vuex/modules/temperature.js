import {
  ADD_TEMPERATURES,
  SELECT_TEMPERATURE
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
      labels: [],
      options: {},
      datasets: [{}]
    },
    {
      id: 2,
      name: 'temp 55',
      labels: [],
      options: {},
      datasets: [{}]
    }
  ],
  selectedSensor: {}
}

// mutations
const mutations = {
  [ADD_TEMPERATURES] (state, itemId, value) {
    const record = state.added.find(p => p.id === itemId)
    if (record) {
      record.datasets.data.push(value)
    }
  },
  [SELECT_TEMPERATURE] (state, itemId) {
    state.selectedSensor = state.items.find(p => p.id === itemId)
    state.selectedSensor.labels = ['1', '2', 'as', 'asd', 'asd']
    state.selectedSensor.datasets[0].data = [1, 2, 3, 4, 5]
  }
}

export default {
  state,
  mutations
}
