#!/usr/bin/python
import time
from sockets.ws_cgi import wscgi
from hal.digital_outputs import JouleDigitalOutputs
import logging

if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG)
  outputs = JouleDigitalOutputs()
  ws = wscgi()

  while True:
    time.sleep(100)

