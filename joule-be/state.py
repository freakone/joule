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

    for m in modules:
      m.set_status_cb(self.status_changed_cb)

    self.digital_inputs.set_cb(self.di_changed)

  def di_changed(self, dinput):
    if self.digital_inputs.input_state(di_map.EMERGENCY_NO) == self.digital_inputs.input_state(di_map.EMERGENCY_NC):
      self.set_current_state(state.EMERGENCY_STOP)
      print "EMERGENCY BUTTON signal error"
      return

    if self.digital_inputs.input_state(di_map.EMERGENCY_NO):
      self.set_current_state(state.EMERGENCY_STOP)
      return

  def set_current_state(self, state):
    self.state_map['mode'] = state
    self.leds.set_blink(state)

  def current_state(self):
    return self.state_map['mode']

  def status_changed_cb(self, source):
    # if source.get_status() ==
    print source.__class__.__name__