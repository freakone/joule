import Vue from 'vue'
import App from './App'
import VueCharts from 'vue-charts'
import { sync } from 'vuex-router-sync'
import store from './vuex/store'
import Router from 'vue-router'
import CurrentParameters from './components/current-parameters'
import Temperatures from './components/temperatures'
import Control from './components/control'
import Settings from './components/settings'

require('expose?$!expose?jQuery!jquery')
require('jquery-ui')
require('assets/bootstrap/js/bootstrap.min.js')
require('assets/admin-lte/js/app.js')
require('assets/moment-with-locales.min.js')
require('assets/moment-timezone-with-data.min.js')
require('assets/bootstrap-datetimepicker.min.js')
require('assets/bootstrap-datetimepicker.css')
var VueMdl = require('assets/vue-mdl.min.js')

Vue.use(VueCharts)
Vue.use(Router)
Vue.use(VueMdl.default)

var router = new Router({
  history: false
})

sync(store, router)

router.map({
  '/parameters': {
    name: 'currentParameters',
    component: CurrentParameters
  },
  '/temperatures': {
    name: 'temperaturesHistory',
    component: Temperatures
  },
  '/control': {
    name: 'control',
    component: Control
  },
  '/settings': {
    name: 'settings',
    component: Settings
  }
})

router.beforeEach(function () {
  window.scrollTo(0, 0)
})

router.redirect({
  '*': '/parameters'
})

router.start(App, '#app')
