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
  manual_mode: false,
  error: false,
  error_text: '',
  error_source: '',
  safety_switch: false,
  regulator_mode: states.INITIALIZATION
}

// mutations
const mutations = {
  [RECEIVE_STATE] (state, value) {
    state.name = value.name
    state.mode = value.mode
    state.manual_mode = value.mode === states.MANUAL
    state.safety_switch = value.mode === states.EMERGENCY_STOP
    state.error = value.mode === states.ERROR
    state.error_text = value.error
    state.error_source = value.error_source
    state.regulator_mode = value.regulator_mode
  },
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
