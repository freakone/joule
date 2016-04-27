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
