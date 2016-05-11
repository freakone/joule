#!/usr/bin/python
import time
from sockets.ws_cgi import wscgi
from hal.digital_outputs import JouleDigitalOutputs
from hal.analog_inputs import JouleAnalogInputs
from hal.jowenta import JouleJowenta
from hal.actions import JouleActions
from hal.digital_inputs import JouleDigitalInputs
from hal.temperature import JouleTemperature

import logging

if __name__ == '__main__':
  # logging.basicConfig(level=logging.DEBUG)
  outputs = JouleDigitalOutputs()
  ainputs = JouleAnalogInputs()
  dinputs = JouleDigitalInputs()
  jowenta = JouleJowenta(ainputs)
  temperature = JouleTemperature()

  actions = JouleActions(outputs, jowenta, dinputs, temperature)
  ws = wscgi(actions)

  while True:
    time.sleep(100)

