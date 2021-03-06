import state_map
import globals.states as state
import hal.maps.digital_inputs_map as di_map
import time
from globals.module_mixin import ModuleMixin
import os

class JouleState(ModuleMixin):
  def __init__(self, dinputs, modules):
    super(JouleState, self).__init__()
    self.state_map = self.load_map('state.map', state_map.STATE)
    self.last_state = state.INITIALIZATION
    self.modules = modules
    self.digital_inputs = dinputs
    self.leds = None
    self.emergency_queue = False

    for m in modules:
      m.set_status_cb(self.status_changed_cb)
      self.status_changed_cb(m, m.get_status())

    self.digital_inputs.set_cb(self.di_changed)
    self.di_changed(None)
    if os.environ["JOULELOCAL"] == "1":
      self.set_current_state(state.MANUAL)

  def di_changed(self, dinput):
    if dinput and (dinput['id'] == di_map.EMERGENCY_NC):
      if not self.emergency_queue:
        self.emergency_queue = True
        return
      else:
        self.emergency_queue = False

    if not self.digital_inputs.input_state(di_map.EMERGENCY_NC):
      self.set_current_state(state.EMERGENCY_STOP)
      return

    if self.last_state == state.ERROR:
      self.set_current_state(state.ERROR)
      return

    if self.digital_inputs.input_state(di_map.AUTO_MODE):
      self.set_current_state(state.AUTO)
      return

    self.set_current_state(state.MANUAL)

  def set_current_state(self, state):
    if self.state_map['mode'] == state:
      return

    self.last_state = self.state_map['mode']
    self.state_map['mode'] = state
    if self.leds:
      self.leds.set_blink(state)
    self.cb_call(self.state_map)

  def set_regulator_state(self, state):
    if self.state_map['regulator_mode'] == state:
      return

    self.state_map['regulator_mode'] = state
    self.cb_call(self.state_map)

  def current_state(self):
    return self.state_map['mode']

  def set_leds(self, leds):
    self.leds = leds
    self.leds.set_blink(self.state_map['mode'])

  def status_changed_cb(self, source, last_state):
    if source.get_status() == state.ERROR:
      self.state_map['error_source'] =  source.__class__.__name__
      self.state_map['error'] = source.error_message
      self.set_current_state(state.ERROR)
      print self.state_map

  def set_name(self, name):
    self.state_map['name'] = name
    self.save_map('state.map', self.state_map)
