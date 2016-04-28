import * as types from './mutation-types'

export const selectTemperature = ({ dispatch }, e) => {
  dispatch(types.SELECT_TEMPERATURE, parseInt(e.target.options[e.target.selectedIndex].value))
}

export const setAnalogValue = ({ dispatch }, e) => {
  dispatch(types.UPDATE_ANALOG, parseInt(e.target.id), parseInt(e.target.value))
}

export const setDigitalValue = ({ dispatch }, e) => {
  dispatch(types.UPDATE_OUTPUTS, parseInt(e.target.id), e.target.checked)
}

export const updateName = ({ dispatch }, e) => {
  dispatch(types.UPDATE_NAME, e.target.value)
}

export const updateAnalogOutputName = ({ dispatch }, e) => {
  dispatch(types.UPDATE_ANALOG_NAME, e.target.value)
}

export const updateDigitalOutputName = ({ dispatch }, e) => {
  dispatch(types.UPDATE_DIGITAL_NAME, e.target.value)
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
