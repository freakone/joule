export const analogInputs = state => {
  return state.analog.items
}

export const temperatureSensors = state => {
  return state.temperature.items
}

export const selectedSensor = state => {
  return state.temperature.selectedSensor
}

export const digitalOutputs = state => {
  return state.output.items
}
