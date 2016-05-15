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


  def cb_call(self, cbs, *args):
    for cb in cbs:
      try:
        cb(*args)
      except Exception as e:
        print "cb error", e

  def set_output_cb(self, cb):
    self.output_cb.append(cb)

# callback handling
  def set_output_cb(self, cb):
    self.output_cb.append(cb)

  def set_jowenta_cb(self, cb):
    self.jowenta.set_cb(cb)

  def set_dinput_cb(self, cb):
    self.digital_inputs.set_cb(cb)

  def set_temperature_cb(self, cb):
    self.temperatures.set_cb(cb)

  def set_state_cb(self, cb):
    self.state.set_cb(cb)

# setters

  def set_name(self, name):
    self.state.set_name(name)

  def set_temperature_name(self, id, name):
    self.temperatures.set_name(id, name)

  def set_digital_output_name(self, id, name):
    self.digital_outputs.set_name(id, name)

  def set_jowenta_name(self, id, name):
    self.jowenta.set_name(id, name)

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