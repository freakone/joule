export const analogOutputs = state => {
  return state.analog.items
}

export const temperatureSensors = state => {
  return state.temperature.items
}

export const selectedSensor = state => {
  if (state.temperature.items.length === 0) {
    return {id: 0, datasets: [{data: []}], labels: []}
  }

  if (Object.keys(state.temperature.selectedSensor).length === 0) {
    return state.temperature.items[0]
  }
  return state.temperature.selectedSensor
}

export const digitalOutputs = state => {
  return state.output.items
}

export const digitalInputs = state => {
  return state.dinput.items
}

export const regulatorMode = state => {
  switch (state.general.regulator_mode) {
    case 9:
      return 'ROZPALANIE'
    case 10:
      return 'REGULACJA'
    case 11:
      return 'ZAŁADUNEK'
  }
}

export const generalSettings = state => {
  return state.general
}

export const motors = state => {
  return state.motors.items
}
