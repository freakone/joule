from globals.module_mixin import ModuleMixin
import time
from threading import Thread, Lock
from math import fabs
import globals.states as states
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
    self.fuel_loading_status = states.FUEL_LOADING_PRELOADING

    self.fumes_temp = None
    self.water_temp = None

    self.repumping = 0

    self.jowenta_ton = 0
    self.jowenta_toff = 0
    self.mutex = Lock()

    self.set_status(states.OK)


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

      if self.process_status in [states.IGNITION]:
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
      elif self.process_status in [states.END_OF_FUEL, states.STOP, states.SOFTWARE_STOP, states.FUEL_LOADING]:
        self.actions.set_output(do_map.SMALL_FANS, False)
        self.actions.set_output(do_map.LEFT_FAN, False)
        self.actions.set_output(do_map.RIGHT_FAN, False)
        self.actions.set_motor(ms_map.MAIN_FAN, False)
          
    finally:
        self.mutex.release()

  def set_state(self, stat):
    self.state = stat
    self.state.set_regulator_state(states.STOP)

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
    if cb['id'] == di_map.BUTTON_LEFT and cb['value'] == False and self.process_status in [None, states.STOP]:
      self.set_process_status(states.FUEL_LOADING) ##TEST!
    elif cb['id'] == di_map.BUTTON_LEFT and cb['value'] == False and self.process_status in [states.END_OF_FUEL]:
      self.set_process_status(states.FUEL_LOADING)
    elif cb['id'] == di_map.BUTTON_RIGHT and cb['value'] == False:
      self.set_process_status(states.STOP)

  def fuel_loading_motors_monitoring(self):
    if self.actions.get_input_state(di_map.STOL_DOLNY_OTWARTY):
      self.actions.set_output(do_map.STOL_DOLNY_OPEN, False)

    if self.actions.get_input_state(di_map.STOL_DOLNY_ZAMKNIETY):
      self.actions.set_output(do_map.STOL_DOLNY_CLOSE, False)
      
    if self.actions.get_input_state(di_map.STOL_GORNY_OTWARTY):
      self.actions.set_output(do_map.STOL_GORNY_OPEN, False)
    
    if self.actions.get_input_state(di_map.STOL_GORNY_ZAMKNIETY):
      self.actions.set_output(do_map.STOL_GORNY_CLOSE, False)

  def check_doors(self):
    if (not self.actions.get_input_state(di_map.STOL_GORNY_ZAMKNIETY) or not self.actions.get_input_state(di_map.STOL_DOLNY_ZAMKNIETY)) and not self.actions.get_input_state(di_map.DRZWI_OTWARTE):
      self.actions.set_output(do_map.STOL_GORNY_OPEN, False)
      self.actions.set_output(do_map.STOL_DOLNY_CLOSE, False)
      self.actions.set_output(do_map.STOL_GORNY_CLOSE, False)
      self.actions.set_output(do_map.STOL_DOLNY_OPEN, False)

      self.fuel_loading_status = states.FUEL_LOADING_BOTTOM_TABLE_BACK


  def fuel_loading_check(self):

    self.check_doors()

    prev_state = self.fuel_loading_status

    if self.fuel_loading_status in [states.FUEL_LOADING_PRELOADING, None]:
      self.actions.set_output(do_map.STOL_PODAWCZY, True)
      self.actions.set_output(do_map.DRZWI_OTWORZ, True)
      time.sleep(2)
      self.actions.set_output(do_map.DRZWI_OTWORZ, False)
      self.fuel_loading_status = states.FUEL_LOADING_WAITING_FOR_FUEL

    elif self.fuel_loading_status == states.FUEL_LOADING_WAITING_FOR_FUEL:      
      if self.actions.get_input_state(di_map.BALOT_OBECNY):
        self.actions.set_output(do_map.STOL_PODAWCZY, False)
        self.fuel_loading_status = states.FUEL_LOADING_WAITING_FOR_DOORS

    elif self.fuel_loading_status == states.FUEL_LOADING_WAITING_FOR_DOORS:
      if self.actions.get_input_state(di_map.DRZWI_OTWARTE):
        self.fuel_loading_status = states.FUEL_LOADING_BOTTOM_TABLE
        
        self.actions.set_output(do_map.STOL_DOLNY_CLOSE, False)
        time.sleep(0.5)
        self.actions.set_output(do_map.STOL_DOLNY_OPEN, True)
    
    elif self.fuel_loading_status == states.FUEL_LOADING_BOTTOM_TABLE:      

      if self.actions.get_input_state(di_map.STOL_DOLNY_OTWARTY):
        self.fuel_loading_status = states.FUEL_LOADING_TOP_TABLE

        self.actions.set_output(do_map.STOL_DOLNY_OPEN, False)
        self.actions.set_output(do_map.STOL_GORNY_CLOSE, False)
        time.sleep(0.5)
        self.actions.set_output(do_map.STOL_GORNY_OPEN, True)

    elif self.fuel_loading_status == states.FUEL_LOADING_TOP_TABLE:      
      if self.actions.get_input_state(di_map.STOL_GORNY_OTWARTY):
        self.actions.set_output(do_map.STOL_GORNY_OPEN, False)
        time.sleep(4)
        self.fuel_loading_status = states.FUEL_LOADING_BOTTOM_TABLE_BACK
        self.actions.set_output(do_map.STOL_DOLNY_CLOSE, True)     
      
    elif self.fuel_loading_status == states.FUEL_LOADING_BOTTOM_TABLE_BACK:
      if self.actions.get_input_state(di_map.STOL_DOLNY_ZAMKNIETY):
        self.actions.set_output(do_map.STOL_DOLNY_CLOSE, False)

        self.actions.set_output(do_map.STOL_GORNY_OPEN, False)
        time.sleep(0.5)
        self.actions.set_output(do_map.STOL_GORNY_CLOSE, True)  
        self.fuel_loading_status = states.FUEL_LOADING_TOP_TABLE_BACK
      else:
        self.actions.set_output(do_map.STOL_DOLNY_CLOSE, True)     

    elif self.fuel_loading_status == states.FUEL_LOADING_TOP_TABLE_BACK:
      if self.actions.get_input_state(di_map.STOL_GORNY_ZAMKNIETY):
        self.fuel_loading_status = states.FUEL_LOADING_CLOSE_DOORS

        self.actions.set_output(do_map.DRZWI_ZAMKNIJ, True)
        time.sleep(2)
        self.actions.set_output(do_map.DRZWI_ZAMKNIJ, False)

    elif self.fuel_loading_status == states.FUEL_LOADING_CLOSE_DOORS:
      if self.actions.get_input_state(di_map.DRZWI_ZAMKNIETE):
        self.fuel_loading_status = None
        self.process_status = states.INITIALIZATION
        self.set_process_status(states.STOP)
      
    if self.fuel_loading_status != prev_state:
      print "STATUS ZALADUNKU:", self.fuel_loading_status

  def regulation_loop(self):
    while True:
      self.fuel_loading_motors_monitoring()

      if not self.actions == None and not self.state == None:
        if self.state.current_state() == states.AUTO:
          if self.process_status in [None, states.STOP]: # start apeczki
            time.sleep(0.5)
        #  elif self.water_temp['currentValue'] > self.water_temp['limitMax']:
            #print "#WATER TEMP", self.water_temp['currentValue'], self.water_temp['limitMax']
        #    self.set_process_status(states.SOFTWARE_STOP)
          else:
            if self.process_status == states.IGNITION: #rozpalanie, otwarcie jowenty, 10s on, 20s off
              self.jowenta_open()
              if self.fumes_temp['currentValue'] >= self.fumes_temp['limitMin']:
                self.set_process_status(states.NORMAL_OPERATION)
                self.jowenta_stop()
            elif self.process_status == states.NORMAL_OPERATION:
              #normalna operacja za malo = otworz jowente, dobrze = stoj, za duzo = przymknij
              if self.fumes_temp['currentValue'] < self.fumes_temp['limitMax'] * 0.90:
                self.jowenta_open()
              elif self.fumes_temp['currentValue'] > self.fumes_temp['limitMax'] * 1.10:
                self.jowenta_close()
              else:
                self.jowenta_stop()

              if self.fumes_temp['currentValue'] < self.fumes_temp['limitMin']:
                self.set_process_status(states.END_OF_FUEL)
          
          if self.process_status in [states.END_OF_FUEL, states.FUEL_LOADING, states.STOP]:
            self.jowenta_close()
          
          if self.process_status == states.FUEL_LOADING:
            self.fuel_loading_check()
        
        elif self.state.current_state() == states.EMERGENCY_STOP:
          self.process_status = states.STOP
          self.fuel_loading_status = None

        
        if self.state.current_state() == states.STOP or (self.process_status == states.STOP and self.state.current_state() == states.AUTO):
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

      time.sleep(0.2)

  def start_regulator(self):
    self.th_run = Thread(target=self.regulation_loop)
    self.th_run.setDaemon(True)
    self.th_run.start()
