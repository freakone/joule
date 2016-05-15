import hal.maps.digital_outputs_map as do_map
from globals.module_mixin import ModuleMixin
from hal.lib.MCP230xx import MCP23017
import hal.lib.GPIO as GPIO

class JouleDigitalOutputs(ModuleMixin):
  def __init__(self):
    super(JouleDigitalOutputs, self).__init__()

    #map of pins
    self.map = self.load_map('digital_outputs.map', do_map.DIGITAL_OUTPUTS)
    #get unique mcp addresses
    unique_addresses = set(map(lambda x: x['address'], self.map))
    self.gpio_modules = {}

    #init modules
    for addr in unique_addresses:
      self.gpio_modules[addr] = MCP23017(address=addr)

    self.init_ports()
    m.set_status(state.OK)

  def init_ports(self):
    for output in self.map:
      self.gpio_modules[output['address']].setup(output['index'], GPIO.OUT)
      self.gpio_modules[output['address']].output(output['index'], GPIO.LOW)
      output['value'] = False

  def set_output(self, id, value):
    try:
      if type(value) is not bool:
        raise RuntimeError('Value must be boolean!')

      output = filter(lambda out: out['id'] == id, self.map)
      if len(output) == 1:
        output = output[0]
        self.gpio_modules[output['address']].output(output['index'], value)
        output['value'] = value
        self.zero_errors()
        return output
    except Exception as e:
      print "output error", e
      self.error(e.strerror)

  def toggle_output(self, id):
    try:
      output = filter(lambda out: out['id'] == id, self.map)
      if len(output) == 1:
        output = output[0]
        self.gpio_modules[output['address']].output(output['index'], not output['value'])
        output['value'] = not output['value']
        self.zero_errors()
        return output

    except Exception as e:
      print "output error", e
      self.error(e.strerror)


