from globals.module_mixin import ModuleMixin
import time
from threading import Thread
from math import fabs
import globals.states as state

class JouleController(ModuleMixin):
  def __init__(self):
    super(JouleController, self).__init__()

    self.actions = None
    self.state = None

    self.th_run = Thread(target=self.regulation_loop)
    self.th_run.setDaemon(True)
    self.th_run.start()

    self.set_status(state.OK)

  def set_state(self, state):
    self.state = state

  def set_actions(self, actions):
    self.actions = actions

  def regulation_loop(self):
    while True:
      if not self.actions == None and not self.state == None:
        if self.state.current_state() == state.AUTO:
          for i in range(9, 22):
            self.actions.set_output(i, True)
            time.sleep(2)

          for i in range(9, 22):
            self.actions.set_output(i, False)
            time.sleep(2)

      time.sleep(1)
