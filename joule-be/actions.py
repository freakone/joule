import inspect
import globals.states as st

class JouleActions(object):
  def __init__(self, state, digital_outputs, jowenta, digital_inputs, temperatures, motors):
    self.digital_outputs = digital_outputs
    self.digital_inputs = digital_inputs
    self.jowenta = jowenta
    self.temperatures = temperatures
    self.motors = motors
    self.state = state

    self.state.set_cb(self.status_changed)

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
  def status_changed(self, state):
    if self.state.current_state() in [st.ERROR, st.STOP, st.EMERGENCY_STOP]:
      for out in self.digital_outputs.map:
        self.set_output(out['id'], False)

  def set_motor_cb(self, cb):
    self.motors.set_cb(cb)

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

# getters
  def get_output_state(self, id):
    return self.digital_outputs.output_state(id)

  def get_motor_state(self, id):
    return self.motors.output_state(id)

# setters
  def set_name(self, name):
    self.state.set_name(name)

  def set_temperature_name(self, id, name):
    self.temperatures.set_name(id, name)

  def set_digital_input_name(self, id, name):
    self.digital_inputs.set_name(id, name)

  def set_digital_output_name(self, id, name):
    self.digital_outputs.set_name(id, name)

  def set_jowenta_name(self, id, name):
    self.jowenta.set_name(id, name)

  def set_jowenta_value(self, id, value):
    self.jowenta.set_value(id, value)

  def check_call_source(self, path):
    return 'sockets' in path

  def set_motor(self, id, value):
    if self.check_call_source(inspect.stack()[1][1]) and self.state.current_state() == st.AUTO:
      print "outputs change forbidden during automatic mode"
      return

    if not self.get_motor_state(id) == value:
      _map = self.motors.set_output(id, value)

  def set_output(self, id, value):
    if self.check_call_source(inspect.stack()[1][1]) and self.state.current_state() == st.AUTO:
      print "outputs change forbidden during automatic mode"
      return

    if not self.get_output_state(id) == value:
      _map = self.digital_outputs.set_output(id, value)
      self.cb_call(self.output_cb, _map)

  def toggle_output(self, id):
    _map = self.digital_outputs.toggle_output(id)
    self.cb_call(self.output_cb, _map)