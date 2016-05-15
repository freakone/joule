#!/usr/bin/python
import time
from sockets.ws_cgi import wscgi
from hal.digital_outputs import JouleDigitalOutputs
from hal.analog_inputs import JouleAnalogInputs
from hal.jowenta import JouleJowenta
from actions import JouleActions
from hal.digital_inputs import JouleDigitalInputs
from hal.temperature import JouleTemperature
from hal.status_leds import JouleLeds
from state import JouleState
import RPi.GPIO as GPIO
import logging
import log

def restart_i2c_modules():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(17, GPIO.OUT)
  GPIO.output(17, GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(17, GPIO.LOW)

if __name__ == '__main__':
  # logging.basicConfig(level=logging.DEBUG)
  restart_i2c_modules()
  ainputs = JouleAnalogInputs()
  dinputs = JouleDigitalInputs()
  outputs = JouleDigitalOutputs()
  jowenta = JouleJowenta(ainputs)
  temperature = JouleTemperature()

  state = JouleState(dinputs, [ainputs, dinputs, outputs, jowenta, temperature])
  actions = JouleActions(state, outputs, jowenta, dinputs, temperature)
  leds = JouleLeds(actions)
  state.set_leds(leds)

  ws = wscgi(actions)

  while True:
    time.sleep(100)

