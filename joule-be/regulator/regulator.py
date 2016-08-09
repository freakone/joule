from globals.module_mixin import ModuleMixin
import time
from threading import Thread
from math import fabs
import globals.states as state
import hal.maps.digital_inputs_map as di_map
import hal.maps.digital_outputs_map as do_map

class JouleController(ModuleMixin):
  def __init__(self):
    super(JouleController, self).__init__()

    self.actions = None
    self.state = None

    self.th_run = Thread(target=self.regulation_loop)
    self.th_run.setDaemon(True)
    self.th_run.start()

    self.th_star = None
    self.set_status(state.OK)

  def set_state(self, state):
    self.state = state

  def set_actions(self, actions):
    self.actions = actions
    self.actions.set_dinput_cb(self.dinput_cb)

  def dinput_cb(self, args):
    if not self.actions == None and not self.state == None:
        if self.state.current_state() == state.AUTO:
          if self.th_star == None:
            self.th_star = Thread(target=self.star_loop)
            self.th_star.setDaemon(True)
            self.th_star.start()

  def star_loop(self):
    # self.actions.set_output(do_map.MAIN_AIR_U2, False)
    # self.actions.set_output(do_map.MAIN_AIR_U1, False)
    # time.sleep(5)

    # self.actions.set_output(do_map.MAIN_AIR_U1, True)
    # time.sleep(15)
    # self.actions.set_output(do_map.MAIN_AIR_U1, False)
    # time.sleep(0.5)
    # self.actions.set_output(do_map.MAIN_AIR_U2, True)
    # self.actions.set_output(do_map.MAIN_AIR_U1, True)
    self.th_star = None

  def regulation_loop(self):
    while True:
      if not self.actions == None and not self.state == None:
        if self.state.current_state() == state.AUTO:
          time.sleep(1)
          # for i in range(9, 22):
          #   if self.state.current_state() == state.AUTO:
          #     self.actions.set_output(i, True)
          #     time.sleep(2)

      time.sleep(0.5)
