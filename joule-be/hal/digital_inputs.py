import hal.maps.digital_inputs_map as di_map
from globals.module_mixin import ModuleMixin
from hal.lib.MCP230xx import MCP23017
import hal.lib.GPIO as GPIO
from threading import Thread
import time
import globals.state as state

class JouleDigitalInputs(ModuleMixin):
  def __init__(self):
    super(JouleDigitalInputs, self).__init__()

    #map of pins
    self.map = self.load_map('digital_inputs.map', di_map.DIGITAL_INPUTS)
    #get unique mcp addresses
    unique_addresses = set(map(lambda x: x['address'], self.map))
    self.gpio_modules = {}

    #init modules
    for addr in unique_addresses:
      self.gpio_modules[addr] = MCP23017(address=addr)

    self.init_ports()
    self.measure()

    self.th_run = Thread(target=self.measure_loop)
    self.th_run.setDaemon(True)
    self.th_run.start()

    self.set_status(state.OK)

  def init_ports(self):
    for dinput in self.map:
      self.gpio_modules[dinput['address']].setup(dinput['index'], GPIO.IN)
      dinput['value'] = False

  def input_state(self, id):
    dinput = filter(lambda dinput: dinput['id'] == id, self.map)
    if len(dinput) == 1:
      return not dinput[0]['value']

  def measure(self):
    try:
      for k, v in self.gpio_modules.iteritems():
        single_module = filter(lambda dinput: dinput['address'] == k, self.map)
        pins = map(lambda x: x['index'], single_module)
        pins = self.gpio_modules[k].input_pins(pins)

        for i, result in enumerate(pins):
          if not self.map[i]['value'] == result:
            self.map[i]['value'] = result
            self.cb_call(self.map[i])

        self.zero_errors()
    except Exception as e:
      print "measure error", e
      self.error(e.strerror)

  def measure_loop(self):
    while True:
      self.measure()
      time.sleep(0.1)

