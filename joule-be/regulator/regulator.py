from globals.module_mixin import ModuleMixin
import time
from threading import Thread
from math import fabs
import globals.states as state
import hal.maps.temperature_map as t_map
import hal.maps.digital_inputs_map as di_map
import hal.maps.digital_outputs_map as do_map

class JouleController(ModuleMixin):
  def __init__(self):
    super(JouleController, self).__init__()

    self.actions = None
    self.state = None
    self.process_status = None

    self.fumes_temp = None

    self.jowenta_ton = 0
    self.jowenta_toff = 0
    self.loading_mock = 0

    self.set_status(state.OK)


  def set_process_status(self, status):
    self.process_status = status
    self.state.set_regulator_state(status)

  def set_state(self, state):
    self.state = state

  def set_actions(self, actions):
    self.actions = actions
    self.actions.set_temperature_cb(self.temperature_change)

  def temperature_change(self, cb):
    if cb['id'] == t_map.FUMES:
      self.fumes_temp = cb

  def jowenta_open(self):
    if self.jowenta_ton < 10:
      self.actions.set_output(do_map.JOWENTA_AIR_MAIN_ON, True)
      self.actions.set_output(do_map.JOWENTA_AIR_MAIN_DIR, True)
      self.jowenta_ton = self.jowenta_ton + 1
    else:
      self.actions.set_output(do_map.JOWENTA_AIR_MAIN_ON, False)
      self.jowenta_toff = self.jowenta_toff + 1
      if self.jowenta_toff > 20:
        self.jowenta_ton = 0
        self.jowenta_toff = 0

  def jowenta_close(self):
    if self.jowenta_ton < 10:
      self.actions.set_output(do_map.JOWENTA_AIR_MAIN_ON, True)
      self.actions.set_output(do_map.JOWENTA_AIR_MAIN_DIR, False)
      self.jowenta_ton = self.jowenta_ton + 1
    else:
      self.actions.set_output(do_map.JOWENTA_AIR_MAIN_ON, False)
      self.jowenta_toff = self.jowenta_toff + 1
      if self.jowenta_toff > 20:
        self.jowenta_ton = 0
        self.jowenta_toff = 0

  def jowenta_stop(self):
    self.actions.set_output(do_map.JOWENTA_AIR_MAIN_ON, False)

  def regulation_loop(self):
    while True:
      if not self.actions == None and not self.state == None:
        if self.state.current_state() == state.AUTO:
          if self.process_status == None: # start apeczki
            if not self.fumes_temp == None:
              if self.fumes_temp['currentValue'] < self.fumes_temp['limitMin']:
                self.set_process_status(state.IGNITION)
              else:
                self.set_process_status(state.NORMAL_OPERATION)
          else:
            if self.process_status == state.IGNITION: #rozpalanie, otwarcie jowenty, 10s on, 20s off
              self.jowenta_open()
              if self.fumes_temp['currentValue'] >= self.fumes_temp['limitMax']:
                self.set_process_status(state.NORMAL_OPERATION)
                self.jowenta_stop()
            elif self.process_status == state.NORMAL_OPERATION:
              #normalna operacja za malo = otworz jowente, dobrze = stoj, za duzo = przymknij
              if self.fumes_temp['currentValue'] < self.fumes_temp['limitMax'] * 0.95:
                self.jowenta_open()
              elif self.fumes_temp['currentValue'] > self.fumes_temp['limitMax'] * 1.05:
                self.jowenta_close()
              else:
                self.jowenta_stop()

              if self.fumes_temp['currentValue'] < self.fumes_temp['limitMin']:
                sself.set_process_status(state.END_OF_FUEL)
            elif self.process_status == state.END_OF_FUEL:
              self.loading_mock = self.loading_mock + 1

              if self.loading_mock > 10:
                self.set_process_status(state.NORMAL_OPERATION)

      time.sleep(1)

  def start_regulator(self):
    self.th_run = Thread(target=self.regulation_loop)
    self.th_run.setDaemon(True)
    self.th_run.start()
