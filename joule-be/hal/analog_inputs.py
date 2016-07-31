import hal.maps.analog_inputs_map as ai_map
import os
import time
from threading import Thread
from math import fabs
import globals.state as state
from globals.module_mixin import ModuleMixin
import random

if not os.environ["JOULELOCAL"] == "1":
  from hal.lib.MCP342x import MCP342x
  import hal.lib.smbus as smbus
  import hal.lib.GPIO as GPIO

class JouleAnalogInputs(ModuleMixin):
  def __init__(self):
    super(JouleAnalogInputs, self).__init__()

    self.map = self.load_map('analog_inputs.map', ai_map.ANALOG_INPUTS)

    if not os.environ["JOULELOCAL"] == "1":
      self.bus = smbus.SMBus(1)
      self.adcs = []

      for ai in self.map:
        self.adcs.append(MCP342x(self.bus, ai['address'], channel=ai['index'], resolution=12))

      self.th_run = Thread(target=self.measure_loop)
    else:
      self.th_run = Thread(target=self.mock_loop)


    self.th_run.setDaemon(True)
    self.th_run.start()
    self.set_status(state.OK)


  def mock_loop(self):
    while True:
      for m in self.map:
        m['value'] = random.uniform(0, 2)
        self.cb_call(m)
      time.sleep(1)


  def measure_loop(self):
    while True:
      try:
        results = MCP342x.convert_and_read_many(self.adcs, samples=1)
        for i, result in enumerate(results):
          result = result[0]
          if fabs(result - self.map[i]['value']) > 0.01:
            self.map[i]['value'] = result
            self.cb_call(self.map[i])
        self.zero_errors()

      except Exception as e:
        print "measure error", e
        self.error(str(e))

      time.sleep(0.1)