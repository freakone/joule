import os
import hal.maps.motor_starter_map as m_map
from globals.module_mixin import ModuleMixin
import time
from threading import Thread
from math import fabs
import globals.states as state

class JouleMotor(ModuleMixin):
  def __init__(self):
    super(JouleMotor, self).__init__()

    self.map = self.load_map('motor.map', m_map.MOTORS)
    self.actions = None
    self.state = None
    self.set_status(state.OK)

    self.stop_during_start = False

  def set_state(self, state):
    self.state = state

  def set_actions(self, actions):
    self.actions = actions

  def star_routine(self, motor):
    motor['starting'] = True
    self.cb_call(motor)
    self.actions.set_output(motor['gpio_u1'], True)
    time.sleep(15)
    self.actions.set_output(motor['gpio_u1'], False)
    time.sleep(0.050)
    self.actions.set_output(motor['gpio_u2'], True)
    self.actions.set_output(motor['gpio_u1'], True)
    motor['starting'] = False
    motor['value'] = True

    if self.stop_during_start:
      self.actions.set_output(motor['gpio_u2'], False)
      self.actions.set_output(motor['gpio_u1'], False)
      motor['starting'] = False
      motor['value'] = False
      self.stop_during_start = False


    self.cb_call(motor)

  def output_state(self, id):
    doutput = filter(lambda doutput: doutput['id'] == id, self.map)
    if len(doutput) == 1:
      return doutput[0]['value']

  def set_output(self, id, value):
    # if os.environ["JOULELOCAL"] == "1":
    #   print "wanna set some motor output", id, value
    #   output = filter(lambda out: out['id'] == id, self.map)[0]
    #   output['value'] = value
    #   return output

    try:
      if type(value) is not bool:
        raise RuntimeError('Value must be boolean!')

      output = filter(lambda out: out['id'] == id, self.map)
      if len(output) == 1:
        output = output[0]

        if not self.stop_during_start:
          if not output['starting'] and not output["value"] and value:
            th_run = Thread(target=self.star_routine, args=[output])
            th_run.start()
          elif output["value"] and not output["starting"] and not value:
            self.actions.set_output(output['gpio_u2'], False)
            self.actions.set_output(output['gpio_u1'], False)
            output['starting'] = False
            output['value'] = False
            self.cb_call(output)
          elif output["starting"] and not value:
            self.stop_during_start = True        

        self.zero_errors()
        return output
    except Exception as e:
      print "output error", e
      self.error(str(e))

  def set_name(self, id, name):
    output = filter(lambda out: out['id'] == id, self.map)
    if len(output) == 1:
      output[0]['name'] = name
      self.save_map('motor.map', self.map)

  def set_value(self, id, value):
    output = filter(lambda out: out['id'] == id, self.map)
    if len(output) == 1:
      output[0]['value'] = value
      self.cb_call(output[0])
      self.save_map('motor.map', self.map)

