import hal.maps.digital_inputs_map as do_map
from globals.module_mixin import ModuleMixin
from hal.lib.MCP230xx import MCP23017
import hal.lib.GPIO as GPIO
from threading import Thread
import time

class JouleDigitalInputs(ModuleMixin):
  def __init__(self):
    super(JouleDigitalInputs, self).__init__()

    #map of pins
    # self.map = self.load_map('digital_outputs.map', do_map.DIGITAL_OUTPUTS)
    self.map = do_map.DIGITAL_INPUTS
    #get unique mcp addresses
    unique_addresses = set(map(lambda x: x['address'], self.map))
    self.gpio_modules = {}

    #init modules
    for addr in unique_addresses:
      self.gpio_modules[addr] = MCP23017(address=addr)

    self.init_ports()

    self.th_run = Thread(target=self.measure_loop)
    self.th_run.setDaemon(True)
    self.th_run.start()

  def init_ports(self):
    for dinput in self.map:
      self.gpio_modules[dinput['address']].setup(dinput['index'], GPIO.IN)
      dinput['value'] = False

  def input_state(self, id):
    dinput = filter(lambda dinput: dinput['id'] == id, self.map)
    if len(dinput) == 1:
      return dinput[0]['value']

  def measure_loop(self):
    while True:
      try:
        for k, v in self.gpio_modules.iteritems():
          single_module = filter(lambda dinput: dinput['address'] == k, self.map)
          pins = map(lambda x: x['index'], single_module)
          pins = self.gpio_modules[k].input_pins(pins)

          for i, result in enumerate(pins):
            if not self.map[i]['value'] == result:
              self.map[i]['value'] = result
              self.cb_call(self.map[i])

      except Exception as e:
        print "measure error", e

      time.sleep(0.1)

