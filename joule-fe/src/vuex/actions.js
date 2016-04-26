import * as types from './mutation-types'

export const selectTemperature = ({ dispatch }, e) => {
  dispatch(types.SELECT_TEMPERATURE, parseInt(e.target.options[e.target.selectedIndex].value))
}
