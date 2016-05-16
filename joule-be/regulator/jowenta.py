import hal.maps.jowenta_map as j_map
from globals.module_mixin import ModuleMixin
import time
from threading import Thread
from math import fabs
import globals.states as state

class JouleJowenta(ModuleMixin):
  def __init__(self, analog_inputs):
    super(JouleJowenta, self).__init__()

    self.map = self.load_map('jowenta.map', j_map.JOWENTA)
    self.actions = None
    self.state = None

    for m in analog_inputs.map:
      self.ainput_changed(m)

    analog_inputs.set_cb(self.ainput_changed)

    self.th_run = Thread(target=self.regulation_loop)
    self.th_run.setDaemon(True)
    self.th_run.start()

    self.set_status(state.OK)

  def set_state(self, state):
    self.state = state

  def set_actions(self, actions):
    self.actions = actions

  def ainput_changed(self, ainput):
    value = ainput['value'] - ainput['min']
    value = value / (ainput['max'] - ainput['min'])
    value = int(value * 100)

    jowenta = filter(lambda x: x['id'] == ainput['id'], self.map)
    if len(jowenta) == 1:
      jowenta = jowenta[0]
      jowenta['actual_value'] = value
      self.cb_call(jowenta)

  def regulation_loop(self):
    while True:
      if not self.actions == None and not self.state == None:
        if self.state.current_state() == state.AUTO or self.state.current_state() == state.MANUAL:
          for j in self.map:
            if fabs(j['value'] - j['actual_value']) > 5:
              if j['value'] > j['actual_value']:
                self.actions.set_output(j['gpio_dir'], True)
              else:
                self.actions.set_output(j['gpio_dir'], False)

              self.actions.set_output(j['gpio_power'], True)
            else:
              self.actions.set_output(j['gpio_dir'], False)
              self.actions.set_output(j['gpio_power'], False)

      time.sleep(0.2)

  def set_name(self, id, name):
    output = filter(lambda out: out['id'] == id, self.map)
    if len(output) == 1:
      output[0]['name'] = name
      self.save_map('jowenta.map', self.map)

  def set_value(self, id, value):
    output = filter(lambda out: out['id'] == id, self.map)
    if len(output) == 1:
      output[0]['value'] = value
      self.cb_call(output[0])
      self.save_map('jowenta.map', self.map)

