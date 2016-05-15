import {
  UPDATE_NAME,
  UPDATE_LOADING,
  UPDATE_MANUAL_MODE,
  RECEIVE_STATE
} from '../mutation-types'

import * as states from '../../api/states'

const state = {
  name: 'BEM 852',
  mode: states.INITIALIZATION,
  loading: false,
  manual_mode: true
}

// mutations
const mutations = {
  [RECEIVE_STATE] (state, value) {
    state.name = value.name
    state.mode = value.mode
    state.manual_mode = value.mode === states.MANUAL
  },
  [UPDATE_NAME] (state, value) {
    state.general_state.name = value
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
