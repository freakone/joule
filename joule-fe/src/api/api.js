var io = require('socket.io-client')
var socket = ''
import * as actions from '../vuex/actions'

export default {
  setDigitalValue (id, value) {
    socket.emit('set_digital', {id: id, value: value})
  },
  setName (name) {
    socket.emit('set_name', name)
  },
  setDigitalOuputName (id, value) {
    socket.emit('set_digital_output_name', {id: id, value: value})
  },
  setTemperatureName (id, value) {
    socket.emit('set_temperature_name', {id: id, value: value})
  },
  setJowentaName (id, value) {
    socket.emit('set_jowenta_name', {id: id, value: value})
  },
  updateJowentaValue (id, value) {
    socket.emit('set_jowenta_value', {id: id, value: value})
  },
  initialize (store) {
    socket = io('http://192.168.2.1:5000/msgbus')

    socket.on('connected', () => {
      console.log("I'm connected")
    })

    socket.on('digital_output_init', (data) => {
      actions.initDigitalOutputs(store, data)
    })

    socket.on('digital_output_changed', (data) => {
      actions.updateDigitalValueSilently(store, data.id, data.value)
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

    socket.on('temperature_init', (data) => {
      actions.initTemperature(store, data)
    })

    socket.on('temperature_changed', (data) => {
      actions.addTemperature(store, data)
    })

    socket.on('state_init', (data) => {
      actions.updateState(store, data)
    })

    socket.on('state_changed', (data) => {
      actions.updateState(store, data)
    })
  }
}
