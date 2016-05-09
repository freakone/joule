import hal.maps.digital_outputs_map as do_map


class JouleActions(object):

  def __init__(self, digital_outputs):
    self.digital_outputs = digital_outputs
    self.output_cb = []

  def set_output_cb(self, cb):
    self.output_cb += cb

  def set_output(self, id, value):
    self.digital_outputs.set_output(id, value)
    if self.output_cb:
      for cb in self.output_cb:
        cb(do_map.DIGITAL_OUTPUTS)