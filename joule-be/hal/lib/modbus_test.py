import RPi.GPIO as GPIO
import serial
import time

GPIO.setmode(GPIO.BCM)
import minimalmodbus

minimalmodbus.BAUDRATE = 9600
minimalmodbus.TIMEOUT = 0.3
instrument = minimalmodbus.Instrument('/dev/ttyAMA0', 1, 18)

while True:
  temperature = instrument.read_register(52, 1)
  print temperature
  time.sleep(0.5)
