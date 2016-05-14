import globals.state as state
import pickle

class ModuleMixin(object):
  def __init__(self):
    self.status = state.INITIALIZATION
    self.status_cb = None
    self.error_code = 0
    self.cb = []

  def set_cb(self, cb):
    self.cb.append(cb)

  def cb_call(self, *args):
    for cb in self.cb:
      try:
        cb(*args)
      except Exception as e:
        print e

  def set_status_cb(self, cb):
    self.status_cb = cb

  def set_status(self, status):
    self.status = status
    self.status_cb(self)

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