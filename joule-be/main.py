#!/usr/bin/python
import time
import os
os.environ["JOULELOCAL"] = "0"

from sockets.ws_cgi import wscgi
from hal.digital_outputs import JouleDigitalOutputs
from hal.analog_inputs import JouleAnalogInputs
from actions import JouleActions
from hal.digital_inputs import JouleDigitalInputs
from hal.temperature import JouleTemperature
from hal.status_leds import JouleLeds
from regulator.motor_starter import JouleMotor
from regulator.jowenta import JouleJowenta
from regulator.regulator import JouleController
from state import JouleState
import logging
import log

def restart_i2c_modules():
  if not os.environ["JOULELOCAL"] == "1":
    import RPi.GPIO as GPIO
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
  temperature = JouleTemperature()

  jowenta = JouleJowenta(ainputs)
  motor = JouleMotor()
  controller = JouleController()

  state = JouleState(dinputs, [ainputs, dinputs, outputs, jowenta, temperature, controller, motor])
  actions = JouleActions(state, outputs, jowenta, dinputs, temperature, motor)
  leds = JouleLeds(actions)

  state.set_leds(leds)
  jowenta.set_actions(actions)
  jowenta.set_state(state)
  motor.set_actions(actions)
  motor.set_state(state)
  controller.set_actions(actions)
  controller.set_state(state)

  ws = wscgi(actions)

  while True:
    time.sleep(100)

