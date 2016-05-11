import hal.maps.jowenta_map as j_map
from globals.module_mixin import ModuleMixin
import time
from threading import Thread
from math import fabs

class JouleJowenta(ModuleMixin):
  def __init__(self, analog_inputs):
    super(JouleJowenta, self).__init__()

    # self.map = self.load_map('analog_inputs.map', ai_map.ANALOG_INPUTS)
    self.map = j_map.JOWENTA
    self.cb = []

    for m in analog_inputs.map:
      self.ainput_changed(m)

    analog_inputs.set_cb(self.ainput_changed)

    self.th_run = Thread(target=self.regulation_loop)
    self.th_run.setDaemon(True)
    self.th_run.start()

  def ainput_changed(self, ainput):
    value = ainput['value'] - ainput['min']
    value = value / (ainput['max'] - ainput['min'])
    value = int(value * 100)

    jowenta = filter(lambda x: x['id'] == ainput['id'], self.map)
    if len(jowenta) == 1:
      jowenta = jowenta[0]
      jowenta['actual_value'] = value
      self.cb_call(jowenta)

  def set_cb(self, cb):
    self.cb.append(cb)

  def cb_call(self, jowenta):
    for cb in self.cb:
      try:
        cb(jowenta)
      except Exception as e:
        print e

  def regulation_loop(self):
    while True:
      time.sleep(0.1)