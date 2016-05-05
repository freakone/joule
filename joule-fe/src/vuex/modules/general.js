import {
  UPDATE_NAME,
  UPDATE_LOADING
} from '../mutation-types'

const state = {
  name: 'BCU-600',
  loading: false
}

// mutations
const mutations = {
  [UPDATE_NAME] (state, value) {
    state.name = value
  },
  [UPDATE_LOADING] (state, value) {
    state.loading = value
  }
}

export default {
  state,
  mutations
}
