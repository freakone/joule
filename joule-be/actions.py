import inspect
import globals.states as st

class JouleActions(object):
  def __init__(self, state, digital_outputs, jowenta, digital_inputs, temperatures):
    self.digital_outputs = digital_outputs
    self.digital_inputs = digital_inputs
    self.jowenta = jowenta
    self.temperatures = temperatures
    self.state = state

    self.output_cb = []
    self.jowenta_cb = []
    self.dinput_cb = []
    self.temperature_cb = []

    jowenta.set_cb(self.jowenta_changed)
    digital_inputs.set_cb(self.di_changed)
    temperatures.set_cb(self.temperature_changed)

# callback handling
  def cb_call(self, cbs, *args):
    for cb in cbs:
      try:
        cb(*args)
      except Exception as e:
        print "cb error", e

  def set_output_cb(self, cb):
    self.output_cb.append(cb)

  def set_jowenta_cb(self, cb):
    self.jowenta_cb.append(cb)

  def set_dinput_cb(self, cb):
    self.dinput_cb.append(cb)

  def set_temperature_cb(self, cb):
    self.temperature_cb.append(cb)

# changed events
  def jowenta_changed(self, jowenta):
    self.cb_call(self.jowenta_cb, jowenta)

  def di_changed(self, dinput):
    self.cb_call(self.dinput_cb, dinput)

  def temperature_changed(self, temperature):
    self.cb_call(self.temperature_cb, temperature)

# setters
  def check_call_source(self, path):
    return 'sockets' in path

  def set_output(self, id, value):
    if self.check_call_source(inspect.stack()[1][1]) and self.state.current_state() == st.AUTO:
      print "outputs change forbidden during automatic mode"
      return

    _map = self.digital_outputs.set_output(id, value)
    self.cb_call(self.output_cb, _map)

  def toggle_output(self, id):
    _map = self.digital_outputs.toggle_output(id)
    self.cb_call(self.output_cb, _map)