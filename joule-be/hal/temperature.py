import hal.maps.temperature_map as t_map
from globals.module_mixin import ModuleMixin
import time
from threading import Thread
from math import fabs
import os
if not os.environ["JOULELOCAL"] == "1":
  import hal.lib.minimalmodbus as modbus
  import RPi.GPIO as GPIO
import globals.state as state

class JouleTemperature(ModuleMixin):
  def __init__(self):
    super(JouleTemperature, self).__init__()

    self.map = self.load_map('temperature.map', t_map.TEMPERATURE)

    if not os.environ["JOULELOCAL"] == "1":
      GPIO.setmode(GPIO.BCM)
      modbus.BAUDRATE = 9600
      modbus.TIMEOUT = 0.3
      #GPIO18 as read/write modifier, module address = 1
      self.module = modbus.Instrument('/dev/ttyAMA0', 1, 18)

      self.th_run = Thread(target=self.measure_loop)
    else:
      self.th_run = Thread(target=self.mock_loop)


    self.th_run.setDaemon(True)
    self.th_run.start()
    self.set_status(state.OK)

  def mock_loop(self):
    while True:
      time.sleep(1)

  def measure_loop(self):
    while True:
      try:
        for t in self.map:
          temp = self.module.read_register(t['register'], 1)
          if fabs(temp - t['currentValue']) > 0.2:
            t['currentValue'] = temp
            self.cb_call(t)

        self.zero_errors()
      except Exception as e:
        print "measure error", e
        self.error(str(e))

      time.sleep(5)

  def set_name(self, id, name):
    output = filter(lambda out: out['id'] == id, self.map)
    if len(output) == 1:
      output[0]['name'] = name
      self.save_map('temperature.map', self.map)