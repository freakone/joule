import * as types from './mutation-types'

export const selectTemperature = ({ dispatch }, itemId) => {
  dispatch(types.SELECT_TEMPERATURE, itemId)
}
