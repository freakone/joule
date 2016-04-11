import Vue from 'vue'
import App from './App'

require('expose?$!expose?jQuery!jquery')
require('assets/admin-lte/js/app.min.js')

/*eslint-disable */
new Vue({
  el: 'body',
  components: { App }
})
