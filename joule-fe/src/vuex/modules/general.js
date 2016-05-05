import {
  UPDATE_NAME,
  UPDATE_LOADING,
  UPDATE_MANUAL_MODE
} from '../mutation-types'

const state = {
  name: 'BCU-600',
  loading: false,
  manual_mode: false
}

// mutations
const mutations = {
  [UPDATE_NAME] (state, value) {
    state.name = value
  },
  [UPDATE_LOADING] (state, value) {
    state.loading = value
  },
  [UPDATE_MANUAL_MODE] (state, value) {
    state.manual_mode = value
  }
}

export default {
  state,
  mutations
}
