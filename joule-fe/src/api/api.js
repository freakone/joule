var io = require('socket.io-client')
var socket = ''
import * as actions from '../vuex/actions'

export default {
  setDigitalValue (id, value) {
    socket.emit('set_digital', {id: id, value: value})
  },
  initialize (store) {
    socket = io('http://192.168.1.105:5000/msgbus')

    socket.on('connected', () => {
      console.log("I'm connected")
    })

    socket.on('digital_output_init', (data) => {
      actions.initDigitalOutputs(store, data)
    })

    socket.on('jowenta_init', (data) => {
      actions.initJowenta(store, data)
    })

    socket.on('jowenta_changed', (data) => {
      actions.updateAnalogActualValue(store, data)
    })

    socket.on('digital_input_init', (data) => {
      actions.initDigitalInputs(store, data)
    })

    socket.on('digital_input_changed', (data) => {
      actions.updateDigitalInput(store, data)
    })
  }
}
