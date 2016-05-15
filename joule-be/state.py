import state_map
import globals.states as state
import hal.maps.digital_inputs_map as di_map
import time

class JouleState(object):
  def __init__(self, leds, dinputs, modules):
    self.state_map = state_map.STATE
    self.modules = modules
    self.digital_inputs = dinputs
    self.leds = leds
    self.emergency_queue = False

    for m in modules:
      m.set_status_cb(self.status_changed_cb)

    self.digital_inputs.set_cb(self.di_changed)
    self.di_changed(None)

  def di_changed(self, dinput):
    if dinput and (dinput['id'] == di_map.EMERGENCY_NO or dinput['id'] == di_map.EMERGENCY_NC):
      if not self.emergency_queue:
        self.emergency_queue = True
        return
      else:
        self.emergency_queue = False

    if self.digital_inputs.input_state(di_map.EMERGENCY_NO) == self.digital_inputs.input_state(di_map.EMERGENCY_NC):
      self.set_current_state(state.EMERGENCY_STOP)
      print "EMERGENCY BUTTON signal error"
      return

    if self.digital_inputs.input_state(di_map.EMERGENCY_NO):
      self.set_current_state(state.EMERGENCY_STOP)
      return

    if self.digital_inputs.input_state(di_map.MANUAL_MODE):
      self.set_current_state(state.MANUAL)
      return

    if self.digital_inputs.input_state(di_map.AUTO_MODE):
      self.set_current_state(state.AUTO)
      return

    self.set_current_state(state.STOP)

  def set_current_state(self, state):
    self.state_map['mode'] = state
    self.leds.set_blink(state)

  def current_state(self):
    return self.state_map['mode']

  def status_changed_cb(self, source):
    # if source.get_status() ==
    print source.__class__.__name__