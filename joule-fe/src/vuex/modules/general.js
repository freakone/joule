import {
  UPDATE_NAME
} from '../mutation-types'

const state = {
  name: 'BCU-600'
}

// mutations
const mutations = {
  [UPDATE_NAME] (state, value) {
    state.name = value
  }
}

export default {
  state,
  mutations
}
