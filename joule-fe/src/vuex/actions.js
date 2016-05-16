import * as types from './mutation-types'
import api from '../api/api'

export const updateLoading = ({ dispatch }, value) => {
  dispatch(types.UPDATE_LOADING, value)
}

// DIGITAL OUTPUTS
export const initDigitalOutputs = ({dispatch}, state) => {
  dispatch(types.RECEIVE_DIGITAL_OUTPUTS, state)
}

export const updateDigitalValueSilently = ({ dispatch }, id, value) => {
  dispatch(types.UPDATE_OUTPUT, id, value)
}

export const updateDigitalValue = ({ dispatch }, e) => {
  var id = parseInt(e.target.id)
  var value = e.target.checked
  dispatch(types.UPDATE_OUTPUT, id, value)
  api.setDigitalValue(id, value)
}

export const updateDigitalOutputName = ({ dispatch }, e) => {
  var id = parseInt(e.target.id)
  dispatch(types.UPDATE_DIGITAL_NAME, id, e.target.value)
  api.setDigitalOuputName(id, e.target.value)
}

// DIGITAL INPUTS
export const initDigitalInputs = ({dispatch}, state) => {
  dispatch(types.RECEIVE_DIGITAL_INPUTS, state)
}

export const updateDigitalInput = ({dispatch}, state) => {
  dispatch(types.UPDATE_DIGITAL_INPUT, state.id, state.value)
}

export const updateDigitalInputName = ({ dispatch }, e) => {
  dispatch(types.UPDATE_DIGITAL_INPUT_NAME, parseInt(e.target.id), e.target.value)
}

// TEMPERATURE
export const updateTemperatureSensorName = ({ dispatch }, e) => {
  var id = parseInt(e.target.id)
  dispatch(types.UPDATE_TEMPERATURE_NAME, id, e.target.value)
  api.setTemperatureName(id, e.target.value)
}

export const updateTemperatureMinimum = ({ dispatch }, e) => {
  dispatch(types.UPDATE_TEMPERATURE_MINIMUM, parseInt(e.target.id), parseInt(e.target.value))
}

export const updateTemperatureMaximum = ({ dispatch }, e) => {
  dispatch(types.UPDATE_TEMPERATURE_MAXIMUM, parseInt(e.target.id), parseInt(e.target.value))
}

export const selectTemperature = ({ dispatch }, e) => {
  dispatch(types.SELECT_TEMPERATURE, parseInt(e.target.options[e.target.selectedIndex].value))
}

export const initTemperature = ({ dispatch }, data) => {
  dispatch(types.RECEIVE_TEMPERATURE_INPUTS, data)
}

export const addTemperature = ({ dispatch }, data) => {
  dispatch(types.ADD_TEMPERATURE, data.id, data.currentValue)
}

// JOWENTA
export const initJowenta = ({dispatch}, state) => {
  dispatch(types.RECEIVE_ANALOG_OUTPUTS, state)
}

export const updateAnalogActualValue = ({dispatch}, state) => {
  dispatch(types.UPDATE_ANALOG_ACTUAL_VALUE, state.id, state.actual_value)
}

export const updateAnalogValue = ({ dispatch }, e) => {
  var id = parseInt(e.target.id)
  var value = parseInt(e.target.value)
  dispatch(types.UPDATE_ANALOG, id, value)
  api.updateJowentaValue(id, value)
}

export const updateAnalogOutputName = ({ dispatch }, e) => {
  var id = parseInt(e.target.id)
  dispatch(types.UPDATE_ANALOG_NAME, parseInt(e.target.id), e.target.value)
  api.setJowentaName(id, e.target.value)
}

// GENERAL STATE
export const updateState = ({dispatch}, state) => {
  dispatch(types.RECEIVE_STATE, state)
}

export const updateName = ({ dispatch }, e) => {
  dispatch(types.UPDATE_NAME, e.target.value)
  api.setName(e.target.value)
}

export const updateManualMode = ({ dispatch }, value) => {
  dispatch(types.UPDATE_MANUAL_MODE, value)
}
