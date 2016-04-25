import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from 'vuex/logger'

import analog from './modules/analog'
import temperature from './modules/temperature'
import output from './modules/output'

Vue.use(Vuex)
Vue.config.debug = true

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    analog,
    temperature,
    output
  },
  strict: debug,
  middlewares: debug ? [createLogger()] : []
})
