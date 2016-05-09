import hal.maps.digital_outputs_map as do_map
from globals.module_mixin import ModuleMixin
from hal.lib.MCP230xx import MCP23017
import hal.lib.GPIO as GPIO

class JouleDigitalOutputs(ModuleMixin):
  def __init__(self):
    super(ModuleMixin, self).__init__()

    #map of pins
    self.map = self.load_map('digital_outputs.map', do_map.DIGITAL_OUTPUTS)

    #get unique mcp addresses
    unique_addresses = set(map(lambda x: x['address'], do_map.DIGITAL_OUTPUTS))
    self.gpio_modules = {}

    #init modules
    for addr in unique_addresses:
      self.gpio_modules[addr] = MCP23017(address=addr)

    self.init_ports()

  def init_ports(self):
    for output in do_map.DIGITAL_OUTPUTS:
      self.gpio_modules[output['address']].setup(output['index'], GPIO.OUT)
      self.gpio_modules[output['address']].output(output['index'], GPIO.LOW)
      output['value'] = False

  def set_output(self, id, value):

    if type(value) is not bool:
      raise RuntimeError('Value must be boolean!')

    output = filter(lambda out: out['id'] == id, do_map.DIGITAL_OUTPUTS)
    if len(output) == 1:
      output = output[0]
      self.gpio_modules[output['address']].output(output['index'], value)
      output['value'] = value
