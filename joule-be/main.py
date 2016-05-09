#!/usr/bin/python
import time
from sockets.ws_cgi import wscgi
from hal.digital_outputs import JouleDigitalOutputs
from hal.actions import JouleActions
import logging

if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG)
  outputs = JouleDigitalOutputs()

  actions = JouleActions(outputs)
  ws = wscgi(actions)

  while True:
    time.sleep(100)

