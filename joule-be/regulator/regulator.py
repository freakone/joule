from globals.module_mixin import ModuleMixin
import time
from threading import Thread, Lock
from math import fabs
import globals.states as state
import hal.maps.temperature_map as t_map
import hal.maps.digital_inputs_map as di_map
import hal.maps.digital_outputs_map as do_map
import hal.maps.motor_starter_map as ms_map

class JouleController(ModuleMixin):
  def __init__(self):
    super(JouleController, self).__init__()

    self.actions = None
    self.state = None
    self.process_status = None

    self.fumes_temp = None
    self.water_temp = None

    self.repumping = 0

    self.jowenta_ton = 0
    self.jowenta_toff = 0
    self.mutex = Lock()

    self.set_status(state.OK)


  def set_process_status(self, status):
    if self.process_status == status:
      return

    self.mutex.acquire()

    try:
      self.process_status = status
      self.jowenta_ton = 0
      self.jowenta_toff = 0
      self.state.set_regulator_state(status)
      print status

      if self.process_status in [state.IGNITION]:
        self.actions.set_output(do_map.PUMP, True)
        time.sleep(5)
        self.actions.set_output(do_map.SMALL_FANS, True)
        time.sleep(1)
        self.actions.set_output(do_map.LEFT_FAN, True)
        time.sleep(1)
        self.actions.set_output(do_map.RIGHT_FAN, True)
        time.sleep(1)
        self.actions.set_motor(ms_map.MAIN_FAN, True)
        time.sleep(5)
      elif self.process_status in [state.END_OF_FUEL, state.STOP, state.SOFTWARE_STOP]:
        self.actions.set_output(do_map.SMALL_FANS, False)
        self.actions.set_output(do_map.LEFT_FAN, False)
        self.actions.set_output(do_map.RIGHT_FAN, False)
        self.actions.set_motor(ms_map.MAIN_FAN, False)
          
    finally:
        self.mutex.release()

  def set_state(self, stat):
    self.state = stat
    self.state.set_regulator_state(state.STOP)

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
      if self.jowenta_toff > 30:
        self.jowenta_ton = 0
        self.jowenta_toff = 0

  def jowenta_stop(self):
    self.actions.set_output(do_map.JOWENTA_AIR_MAIN_ON, False)

  def dinput_cb(self, cb):
    if cb['id'] == di_map.BUTTON_LEFT and cb['value'] == False and self.process_status in [None, state.STOP]:
      self.set_process_status(state.IGNITION)
    elif cb['id'] == di_map.BUTTON_RIGHT and cb['value'] == False:
      self.set_process_status(state.STOP)

  def regulation_loop(self):
    while True:
      if not self.actions == None and not self.state == None:
        if self.state.current_state() == state.AUTO:
          if self.process_status in [None, state.STOP]: # start apeczki
            time.sleep(0.5)
          elif self.water_temp['currentValue'] > self.water_temp['limitMax']:
            #print "#WATER TEMP", self.water_temp['currentValue'], self.water_temp['limitMax']
            self.set_process_status(state.SOFTWARE_STOP)
          else:
            if self.process_status == state.IGNITION: #rozpalanie, otwarcie jowenty, 10s on, 20s off
              self.jowenta_open()
              if self.fumes_temp['currentValue'] >= self.fumes_temp['limitMin']:
                self.set_process_status(state.NORMAL_OPERATION)
                self.jowenta_stop()
            elif self.process_status == state.NORMAL_OPERATION:
              #normalna operacja za malo = otworz jowente, dobrze = stoj, za duzo = przymknij
              if self.fumes_temp['currentValue'] < self.fumes_temp['limitMax'] * 0.90:
                self.jowenta_open()
              elif self.fumes_temp['currentValue'] > self.fumes_temp['limitMax'] * 1.10:
                self.jowenta_close()
              else:
                self.jowenta_stop()

              if self.fumes_temp['currentValue'] < self.fumes_temp['limitMin']:
                self.set_process_status(state.END_OF_FUEL)
            elif self.process_status == state.END_OF_FUEL:
                self.jowenta_stop()
        
        if self.state.current_state() == state.STOP or (self.process_status == state.STOP and self.state.current_state() == state.AUTO):
          if self.water_temp['currentValue'] > 90:
            self.actions.set_output(do_map.PUMP, True)
          elif self.repumping > 0:
            self.actions.set_output(do_map.PUMP, True)
            self.repumping = self.repumping + 1
            if self.repumping > 120:
              self.repumping = 0
              self.actions.set_output(do_map.PUMP, False)
          elif self.water_temp['currentValue'] < 5:
            self.repumping = 1
          elif self.water_temp['currentValue'] < 85:
            self.actions.set_output(do_map.PUMP, False)

      time.sleep(1)

  def start_regulator(self):
    self.th_run = Thread(target=self.regulation_loop)
    self.th_run.setDaemon(True)
    self.th_run.start()
