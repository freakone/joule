var io = require('socket.io-client')
var socket = ''
import * as actions from '../vuex/actions'

export default {
  setDigitalValue (id, value) {
    socket.emit('set_digital', {id: id, value: value})
  },
  setMotorValue (id, value) {
    socket.emit('set_motor', {id: id, value: value})
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
  updateTemperatureMinimum (id, value) {
    socket.emit('set_temperature_minimum', {id: id, value: value})
  },
  updateTemperatureMaximum (id, value) {
    socket.emit('set_temperature_maximum', {id: id, value: value})
  },
  setJowentaName (id, value) {
    socket.emit('set_jowenta_name', {id: id, value: value})
  },
  updateJowentaValue (id, value) {
    socket.emit('set_jowenta_value', {id: id, value: value})
  },
  setDigitalInputName (id, value) {
    socket.emit('set_digital_input_name', {id: id, value: value})
  },
  mock (store) {
    actions.initDigitalOutputs(store, [{id: 9, name: 'P00', value: false},
      {id: 1, name: 'P01', value: false},
      {id: 2, name: 'P02', value: false},
      {id: 3, name: 'P03', value: false},
      {id: 4, name: 'P04', value: true},
      {id: 5, name: 'P05', value: false},
      {id: 6, name: 'P06', value: true},
      {id: 7, name: 'P07', value: false}])
    actions.initJowenta(store, [{id: 1, value: 50, actual_value: 50, name: 'jowenta_dolot'}])
    actions.initDigitalInputs(store, [{id: 1, name: 'switch S1', value: false},
      {id: 2, name: 'switch S2', value: false},
      {id: 3, name: 'switch S3', value: true},
      {id: 4, name: 'switch S4', value: false}])
    actions.initTemperature(store, [{
      id: 1,
      name: 'temperatura palenisko',
      currentValue: 0.0,
      limitMin: 4,
      limitMax: 30,
      labels: ['1', '2', '3', '4'],
      datasets: [{
        backgroundColor: 'rgba(221,75,57,0.6)',
        borderColor: 'rgba(220,75,57,1)',
        data: [25, 26, 27, 22]
      }]
    }
    ])
    actions.updateState(store, {name: 'BEM 123', mode: 6, error: '', error_source: ''})
  },
  initialize (store) {
    // socket = io('http://192.168.2.1:5000/msgbus')
    socket = io('http://192.168.0.90:5000/msgbus')
    // socket = io('http://127.0.0.1:5000/msgbus')

    socket.on('connected', () => {
      console.log("I'm connected")
    })

    socket.on('digital_output_init', (data) => {
      actions.initDigitalOutputs(store, data)
    })

    socket.on('motor_init', (data) => {
      actions.initMotors(store, data)
    })

    socket.on('motor_changed', (data) => {
      actions.updateMotorValueSilently(store, data.id, data.value, data.starting)
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

    socket.on('set_temperature_minimum', (data) => {
      actions.updateTemperatureSensorMinimumSilently(store, data.id, data.value)
    })

    socket.on('set_temperature_maximum', (data) => {
      actions.updateTemperatureSensorMaxmimumSilently(store, data.id, data.value)
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

    socket.on('digital_output_name', (data) => {
      actions.updateDigitalOutputNameSilently(store, data.id, data.value)
    })

    socket.on('digital_input_name', (data) => {
      actions.updateDigitalInputNameSilently(store, data.id, data.value)
    })

    socket.on('temperature_name', (data) => {
      actions.updateTemperatureSensorNameSilently(store, data.id, data.value)
    })

    socket.on('jowenta_name', (data) => {
      actions.updateAnalogOutputNameSilently(store, data.id, data.value)
    })

    socket.on('app_name', (data) => {
      actions.updateNameSilently(store, data)
    })
  }
}
