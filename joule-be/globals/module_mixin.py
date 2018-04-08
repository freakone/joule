import globals.state as state
import pickle

class ModuleMixin(object):
  def __init__(self):
    self.status = state.INITIALIZATION
    self.status_cb = None
    self.error_message = ''
    self.cb = []
    self.map = []
    self.error_counter = 0

  def set_cb(self, cb):
    self.cb.append(cb)

    for m in self.map:
      try:
        cb(m)
      except Exception as e:
        print e

  def cb_call(self, *args):
    for cb in self.cb:
      try:
        cb(*args)
      except Exception as e:
        print e

  def set_status_cb(self, cb):
    self.status_cb = cb

  def zero_errors(self):
    self.error_counter = 0

  def error(self, message):
    self.error_counter = self.error_counter + 1

    if self.error_counter > 20:
      self.error_message = message
      self.set_status(state.ERROR)

  def set_status(self, status):
    last_status = self.status
    self.status = status
    if self.status_cb:
      self.status_cb(self, last_status)

  def get_status(self):
    return self.status

  def save_map(self, filename, _map):
    try:
      pickle.dump(_map, open(filename, "wb+" ))
    except:
      print "map saving error!"

  def load_map(self, filename, _map):
      try:
          return pickle.load(open(filename, "rb" ))
      except:
          self.save_map(filename, _map)
          return _map