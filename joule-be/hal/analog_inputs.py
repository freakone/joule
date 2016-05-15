import hal.maps.analog_inputs_map as ai_map
from globals.module_mixin import ModuleMixin
from hal.lib.MCP342x import MCP342x
import hal.lib.smbus as smbus
import hal.lib.GPIO as GPIO
import time
from threading import Thread
from math import fabs
import globals.state as state

class JouleAnalogInputs(ModuleMixin):
  def __init__(self):
    super(JouleAnalogInputs, self).__init__()

    self.map = self.load_map('analog_inputs.map', ai_map.ANALOG_INPUTS)
    self.bus = smbus.SMBus(1)
    self.adcs = []

    for ai in self.map:
      self.adcs.append(MCP342x(self.bus, ai['address'], channel=ai['index'], resolution=12))

    self.th_run = Thread(target=self.measure_loop)
    self.th_run.setDaemon(True)
    self.th_run.start()
    m.set_status(state.OK)

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
        self.error(e.strerror)

      time.sleep(0.1)