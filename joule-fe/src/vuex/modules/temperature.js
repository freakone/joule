import {
  ADD_TEMPERATURES
} from '../mutation-types'

const initDataset = [{
  backgroundColor: 'rgba(220,220,220,0.9)',
  borderColor: 'rgba(220,220,220,1)',
  borderWidth: 1,
  hoverBackgroundColor: 'rgba(220,220,220,0.5)',
  hoverBorderColor: 'rgba(220,220,220,1)',
  data: [1, 2, 3],
  yAxisID: 'y-axis-0'
}]

const state = {
  items: [
    {
      id: 1,
      name: 'temp1',
      labels: [],
      options: {},
      datasets: initDataset
    },
    {
      id: 2,
      name: 'temp 55',
      labels: [],
      options: {},
      datasets: initDataset
    }
  ]
}

// mutations
const mutations = {
  [ADD_TEMPERATURES] (state, itemId, value) {
    const record = state.added.find(p => p.id === itemId)
    if (record) {
      record.datasets.data.push(value)
    }
  }
}

export default {
  state,
  mutations
}
