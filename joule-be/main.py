#!/usr/bin/python
import time
from sockets.ws_cgi import wscgi
from hal.digital_outputs import JouleDigitalOutputs
from hal.analog_inputs import JouleAnalogInputs
from hal.jowenta import JouleJowenta
from hal.actions import JouleActions
import logging

if __name__ == '__main__':
  # logging.basicConfig(level=logging.DEBUG)
  outputs = JouleDigitalOutputs()
  ainputs = JouleAnalogInputs()
  jowenta = JouleJowenta(ainputs)

  actions = JouleActions(outputs, jowenta)
  ws = wscgi(actions)

  while True:
    time.sleep(100)

