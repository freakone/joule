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
    self.water_temp = None

    self.jowenta_ton = 0
    self.jowenta_toff = 0
    self.loading_mock = 0

    self.set_status(state.OK)


  def set_process_status(self, status):
    if self.process_status == status:
      return

    self.process_status = status
    self.jowenta_ton = 0
    self.jowenta_toff = 0
    self.state.set_regulator_state(status)

  def set_state(self, state):
    self.state = state

  def set_actions(self, actions):
    self.actions = actions
    self.actions.set_temperature_cb(self.temperature_change)
    self.actions.set_dinput_cb(self.dinput_cb)

  def temperature_change(self, cb):
    if cb['id'] == t_map.FUMES:
      self.fumes_temp = cb

    if cb['id'] == t_map.WATER:
      self.water_temp = cb

  def jowenta_open(self):
    # print "otwieranie"
    if self.jowenta_ton < 5:
      self.actions.set_output(do_map.JOWENTA_AIR_MAIN_ON, True)
      self.actions.set_output(do_map.JOWENTA_AIR_MAIN_DIR, False)
      self.jowenta_ton = self.jowenta_ton + 1
    else:
      self.actions.set_output(do_map.JOWENTA_AIR_MAIN_ON, False)
      self.jowenta_toff = self.jowenta_toff + 1
      if self.jowenta_toff > 10:
        self.jowenta_ton = 0
        self.jowenta_toff = 0

  def jowenta_close(self):
    # print "zamykanie"
    if self.jowenta_ton < 5:
      self.actions.set_output(do_map.JOWENTA_AIR_MAIN_ON, True)
      self.actions.set_output(do_map.JOWENTA_AIR_MAIN_DIR, True)
      self.jowenta_ton = self.jowenta_ton + 1
    else:
      self.actions.set_output(do_map.JOWENTA_AIR_MAIN_ON, False)
      self.jowenta_toff = self.jowenta_toff + 1
      if self.jowenta_toff > 10:
        self.jowenta_ton = 0
        self.jowenta_toff = 0

  def jowenta_stop(self):
    self.actions.set_output(do_map.JOWENTA_AIR_MAIN_ON, False)

  def dinput_cb(self, cb):
    if cb['id'] == di_map.BUTTON_LEFT and not self.process_status == None:
      self.set_process_status(state.IGNITION)
      self.loading_mock = 0

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
          elif self.water_temp['currentValue'] > self.water_temp['limitMax']:
            if not self.process_status == state.SOFTWARE_STOP:
              self.set_process_status(state.SOFTWARE_STOP)
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
                self.set_process_status(state.END_OF_FUEL)
            elif self.process_status == state.END_OF_FUEL:
              if self.loading_mock > 45:
                self.jowenta_stop()
              else:
                self.loading_mock = self.loading_mock + 1
                self.actions.set_output(do_map.JOWENTA_AIR_MAIN_ON, True)
                self.actions.set_output(do_map.JOWENTA_AIR_MAIN_DIR, True)

      time.sleep(1)

  def start_regulator(self):
    self.th_run = Thread(target=self.regulation_loop)
    self.th_run.setDaemon(True)
    self.th_run.start()
