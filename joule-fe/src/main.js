import VueMdl from 'vue-mdl'
import Vue from 'vue'
import App from './App'
import VueCharts from 'vue-charts'
import Router from 'vue-router'
import CurrentParameters from './components/current-parameters'
import Temperatures from './components/temperatures'
import Control from './components/control'
import Settings from './components/settings'

require('expose?$!expose?jQuery!jquery')
require('jquery-ui')
require('assets/bootstrap/js/bootstrap.min.js')
require('assets/admin-lte/js/app.js')

Vue.use(VueCharts)
Vue.use(Router)
Vue.use(VueMdl)

var router = new Router({
  history: false,
  hashbang: true
})

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
/*eslint-disable */
// new Vue({
//   el: 'body',
//   components: { App }
// })
