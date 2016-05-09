import time
from threading import Thread
from flask import Flask, render_template
import socketio
import eventlet
eventlet.monkey_patch()

class wscgi(object):
  def __init__(self, actions):
    self.actions = actions
    self.th_server = Thread(target=self.start_server)
    self.th_server.setDaemon(True)
    self.th_server.start()

  def start_server(self):

    sio = socketio.Server(logger=True, async_mode='eventlet')
    app = Flask(__name__)
    app.wsgi_app = socketio.Middleware(sio, app.wsgi_app)
    app.config['SECRET_KEY'] = 'blablablab'

    import protocol
    protocol.protocol_init(sio, self.actions)

    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

