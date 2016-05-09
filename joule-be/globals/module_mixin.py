import globals.state
import pickle

class ModuleMixin(object):
  def __init__(self):
    self.status = state.INITIALIZATION
    self.cb = None
    self.error_code = 0

  def set_status_cb(self, cb):
    self.cb = cb

  def set_status(self, status):
    self.status = status
    self.cb(status, self.error_code)

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