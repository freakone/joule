// const _mocked_init = {
//   digital_outputs: [
//     {
//       id: 1,
//       value: true,
//       name: 'pompa 1'
//     },
//     {
//       id: 2,
//       value: true,
//       name: 'podajnik 1'
//     },
//     {
//       id: 3,
//       value: false,
//       name: 'podajnik 2'
//     }
//   ],
//   analog_outputs: [
//     {
//       id: 1,
//       value: 25,
//       name: 'jowenta dolot'
//     },
//     {
//       id: 2,
//       value: 60,
//       name: 'jowenta wylot'
//     }
//   ],
//   temperature_inputs: [
//     {
//       id: 1,
//       name: 'temperatura palenisko',
//       currentValue: 25,
//       limitMin: 4,
//       limitMax: 30,
//       labels: ['1', '2', 'as', 'asd', 'asd'],
//       options: {},
//       datasets: [{ data: [5, 2, 3, 4, 3] }]
//     },
//     {
//       id: 2,
//       name: 'temperatura plaszcza',
//       currentValue: 230,
//       limitMin: 200,
//       limitMax: 300,
//       labels: ['1', '2', 'as', 'asd', 'asd'],
//       options: {},
//       datasets: [{ data: [1, 2, 3, 4, 5] }]
//     }
//   ],
//   name: 'BCU666',
//   manual_mode: true
// }

var io = require('socket.io-client')
var socket = ''
import { setInitialState } from '../vuex/actions'

export default {
  setDigitalValue (id, value) {
    socket.emit('set_digital', {id: id, value: value})
  },
  initialize (store) {
    socket = io('http://192.168.1.105:5000/msgbus')

    socket.on('connected', () => {
      console.log("I'm connected")
    })

    socket.on('init', (data) => {
      console.log(data)
      setInitialState(store, data)
    })
  }
}
