import os
import hal.maps.digital_outputs_map as do_map
from globals.module_mixin import ModuleMixin
if not os.environ["JOULELOCAL"] == "1":
  from hal.lib.MCP230xx import MCP23017
  import hal.lib.GPIO as GPIO
import globals.state as state

class JouleDigitalOutputs(ModuleMixin):
  def __init__(self):
    super(JouleDigitalOutputs, self).__init__()

    #map of pins
    self.map = self.load_map('digital_outputs.map', do_map.DIGITAL_OUTPUTS)
    #get unique mcp addresses
    unique_addresses = set(map(lambda x: x['address'], self.map))
    self.gpio_modules = {}

    if not os.environ["JOULELOCAL"] == "1":
      #init modules
      for addr in unique_addresses:
        self.gpio_modules[addr] = MCP23017(address=addr)

      self.init_ports()

    self.set_status(state.OK)

  def init_ports(self):
    for output in self.map:
      self.gpio_modules[output['address']].setup(output['index'], GPIO.OUT)
      self.gpio_modules[output['address']].output(output['index'], GPIO.LOW)
      output['value'] = False

  def output_state(self, id):
    doutput = filter(lambda doutput: doutput['id'] == id, self.map)
    if len(doutput) == 1:
      return doutput[0]['value']

  def set_output(self, id, value):

    if os.environ["JOULELOCAL"] == "1":
      print "wanna set some output", id, value
      output = filter(lambda out: out['id'] == id, self.map)[0]
      output['value'] = value
      return output

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
      self.error(str(e))

  def toggle_output(self, id):
    if os.environ["JOULELOCAL"] == "1":
      # print "wanna toggle some output", id
      output = filter(lambda out: out['id'] == id, self.map)[0]
      output['value'] = not output['value']
      return output

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
      self.error(str(e))

  def set_name(self, id, name):
    output = filter(lambda out: out['id'] == id, self.map)
    if len(output) == 1:
      output[0]['name'] = name
      self.save_map('digital_outputs.map', self.map)


