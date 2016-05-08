import * as types from './mutation-types'
import api from '../api/api'

export const updateLoading = ({ dispatch }, value) => {
  dispatch(types.UPDATE_LOADING, value)
}

export const connectWs = ({dispatch}) => {
  api.connectWs()
}

export const getInitialState = ({dispatch}) => {
  dispatch(types.UPDATE_LOADING, true)
  api.getInitialState(state => {
    dispatch(types.RECEIVE_DIGITAL_OUTPUTS, state.digital_outputs)
    dispatch(types.RECEIVE_ANALOG_OUTPUTS, state.analog_outputs)
    dispatch(types.RECEIVE_TEMPERATURE_INPUTS, state.temperature_inputs)
    dispatch(types.UPDATE_NAME, state.name)
    dispatch(types.UPDATE_MANUAL_MODE, state.manual_mode)
    dispatch(types.UPDATE_LOADING, false)
  })
}

export const selectTemperature = ({ dispatch }, e) => {
  dispatch(types.SELECT_TEMPERATURE, parseInt(e.target.options[e.target.selectedIndex].value))
}

export const updateAnalogValue = ({ dispatch }, e) => {
  dispatch(types.UPDATE_ANALOG, parseInt(e.target.id), parseInt(e.target.value))
}

export const updateDigitalValue = ({ dispatch }, e) => {
  dispatch(types.UPDATE_OUTPUTS, parseInt(e.target.id), e.target.checked)
}

export const updateName = ({ dispatch }, e) => {
  dispatch(types.UPDATE_NAME, e.target.value)
}

export const updateManualMode = ({ dispatch }, value) => {
  dispatch(types.UPDATE_MANUAL_MODE, value)
}

export const updateAnalogOutputName = ({ dispatch }, e) => {
  dispatch(types.UPDATE_ANALOG_NAME, parseInt(e.target.id), e.target.value)
}

export const updateDigitalOutputName = ({ dispatch }, e) => {
  dispatch(types.UPDATE_DIGITAL_NAME, parseInt(e.target.id), e.target.value)
}

export const updateTemperatureSensorName = ({ dispatch }, e) => {
  dispatch(types.UPDATE_TEMPERATURE_NAME, parseInt(e.target.id), e.target.value)
}

export const updateTemperatureMinimum = ({ dispatch }, e) => {
  dispatch(types.UPDATE_TEMPERATURE_MINIMUM, parseInt(e.target.id), parseInt(e.target.value))
}

export const updateTemperatureMaximum = ({ dispatch }, e) => {
  dispatch(types.UPDATE_TEMPERATURE_MAXIMUM, parseInt(e.target.id), parseInt(e.target.value))
}
