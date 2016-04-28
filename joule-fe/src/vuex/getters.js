export const analogOutputs = state => {
  return state.analog.items
}

export const temperatureSensors = state => {
  return state.temperature.items
}

export const selectedSensor = state => {
  if (Object.keys(state.temperature.selectedSensor).length === 0) {
    return state.temperature.items[0]
  }
  return state.temperature.selectedSensor
}

export const digitalOutputs = state => {
  return state.output.items
}

export const generalSettings = state => {
  return state.general
}
