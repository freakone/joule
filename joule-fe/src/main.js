import Vue from 'vue'
import App from './App'
import VueCharts from 'vue-charts'

require('expose?$!expose?jQuery!jquery')
require('jquery-ui')
require('assets/bootstrap/js/bootstrap.min.js')
require('assets/admin-lte/js/app.js')

Vue.use(VueCharts)
/*eslint-disable */
new Vue({
  el: 'body',
  components: { App }
})
