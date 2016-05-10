class JouleActions(object):
  def __init__(self, digital_outputs, jowenta):
    self.digital_outputs = digital_outputs
    self.jowenta = jowenta

    self.output_cb = []
    self.jowenta_cb = []

    jowenta.set_cb(self.jowenta_changed)

  def cb_call(self, cbs, *args):
    for cb in cbs:
      try:
        cb(*args)
      except Exception as e:
        print "cb error", e

  def set_output_cb(self, cb):
    self.output_cb.append(cb)

  def set_jowenta_cb(self, cb):
    self.jowenta_cb.append(cb)

  def jowenta_changed(self, jowenta):
    self.cb_call(self.jowenta_cb, jowenta)

  def set_output(self, id, value):
    self.digital_outputs.set_output(id, value)
    for cb in self.output_cb:
      try:
        cb(digital_outputs.map)
      except Exception as e:
        print "cb error", e