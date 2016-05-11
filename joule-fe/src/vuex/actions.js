import * as types from './mutation-types'
import api from '../api/api'

export const updateLoading = ({ dispatch }, value) => {
  dispatch(types.UPDATE_LOADING, value)
}

// DIGITAL OUTPUTS
export const initDigitalOutputs = ({dispatch}, state) => {
  dispatch(types.RECEIVE_DIGITAL_OUTPUTS, state)
}

export const updateDigitalValue = ({ dispatch }, e) => {
  var id = parseInt(e.target.id)
  var value = e.target.checked
  dispatch(types.UPDATE_OUTPUTS, id, value)
  api.setDigitalValue(id, value)
}

export const updateDigitalOutputName = ({ dispatch }, e) => {
  dispatch(types.UPDATE_DIGITAL_NAME, parseInt(e.target.id), e.target.value)
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

//
export const initJowenta = ({dispatch}, state) => {
  dispatch(types.RECEIVE_ANALOG_OUTPUTS, state)
}

export const getInitialState = ({dispatch}, state) => {
  dispatch(types.RECEIVE_TEMPERATURE_INPUTS, state.temperature_inputs)
  dispatch(types.UPDATE_NAME, state.name)
  dispatch(types.UPDATE_MANUAL_MODE, state.manual_mode)
  dispatch(types.UPDATE_LOADING, false)
}

export const selectTemperature = ({ dispatch }, e) => {
  dispatch(types.SELECT_TEMPERATURE, parseInt(e.target.options[e.target.selectedIndex].value))
}

export const updateAnalogActualValue = ({dispatch}, state) => {
  dispatch(types.UPDATE_ANALOG_ACTUAL_VALUE, state.id, state.actual_value)
}

export const updateAnalogValue = ({ dispatch }, e) => {
  dispatch(types.UPDATE_ANALOG, parseInt(e.target.id), parseInt(e.target.value))
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

export const updateTemperatureSensorName = ({ dispatch }, e) => {
  dispatch(types.UPDATE_TEMPERATURE_NAME, parseInt(e.target.id), e.target.value)
}

export const updateTemperatureMinimum = ({ dispatch }, e) => {
  dispatch(types.UPDATE_TEMPERATURE_MINIMUM, parseInt(e.target.id), parseInt(e.target.value))
}

export const updateTemperatureMaximum = ({ dispatch }, e) => {
  dispatch(types.UPDATE_TEMPERATURE_MAXIMUM, parseInt(e.target.id), parseInt(e.target.value))
}
