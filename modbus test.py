import serial
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

ser = serial.Serial(port='/dev/ttyAMA0', baudrate=19200)
ser.isOpen()

GPIO.output(18, GPIO.HIGH)
ser.write('\x01\x01\x00\x01\x91\xD8')
time.sleep(0.5)
GPIO.output(18, GPIO.LOW)

ser.read(5)

# while ser.inWaiting() == 0:
#   print "wait"
#   time.sleep(0.5)

# while ser.inWaitinlg():
#   print ser.read()