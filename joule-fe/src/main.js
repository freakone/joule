import Vue from 'vue'
import App from './App'
import VueCharts from 'vue-charts'
import Router from 'vue-router'
import CurrentParameters from './components/current-parameters'
import Temperatures from './components/temperatures'

require('expose?$!expose?jQuery!jquery')
require('jquery-ui')
require('assets/bootstrap/js/bootstrap.min.js')
require('assets/admin-lte/js/app.js')

Vue.use(VueCharts)
Vue.use(Router)

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
