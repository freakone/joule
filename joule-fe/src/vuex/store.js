import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from 'vuex/logger'

import analog from './modules/analog-output'
import temperature from './modules/temperature'
import output from './modules/digital-output'
import general from './modules/general'
import dinput from './modules/digital-input'
import motors from './modules/motors'

Vue.use(Vuex)
Vue.config.debug = true

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    analog,
    temperature,
    output,
    general,
    dinput,
    motors
  },
  strict: debug,
  middlewares: debug ? [createLogger()] : []
})
