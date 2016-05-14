import globals.states as state
from threading import Thread
import hal.maps.digital_outputs_map as do_map
import time

class JouleLeds(object):
  def __init__(self, actions):
    self.status = state.INITIALIZATION
    self.actions = actions

    self.th_blinker = Thread(target=self.blinker)
    self.th_blinker.setDaemon(True)
    self.th_blinker.start()

  def set_blink(self, status):
    self.status = status
    self.actions.set_output(do_map.LED_GREEN, 0)
    self.actions.set_output(do_map.LED_RED, 0)

    if status == state.AUTO:
      self.actions.set_output(do_map.LED_GREEN, 1)

    if status == state.ERROR:
      self.actions.set_output(do_map.LED_RED, 1)

  def blinker(self):
    while True:
      if self.status == state.MANUAL:
        self.actions.toggle_output(do_map.LED_GREEN)

      if self.status == state.EMERGENCY_STOP:
        self.actions.toggle_output(do_map.LED_RED)

      time.sleep(0.5)
