import time
from threading import Thread
from flask import Flask, render_template
import socketio
import eventlet
eventlet.monkey_patch()
import protocol

class wscgi(object):
  def __init__(self, actions):
    self.actions = actions
    self.sio = None

    self.th_server = Thread(target=self.start_server)
    self.th_server.setDaemon(True)
    self.th_server.start()

    actions.set_jowenta_cb(self.jowenta_changed)
    actions.set_dinput_cb(self.dinput_changed)
    actions.set_temperature_cb(self.temperature_changed)
    actions.set_output_cb(self.doutput_changed)
    actions.set_state_cb(self.state_changed)

  def start_server(self):
    self.sio = socketio.Server(logger=True, async_mode='eventlet')
    app = Flask(__name__)
    app.wsgi_app = socketio.Middleware(self.sio, app.wsgi_app)
    app.config['DEBUG'] = False

    protocol.protocol_init(self.sio, self.actions)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

  def jowenta_changed(self, jowenta):
    self.sio.emit('jowenta_changed', jowenta, namespace='/msgbus')

  def doutput_changed(self, doutput):
    self.sio.emit('digital_output_changed', doutput, namespace='/msgbus')

  def dinput_changed(self, dinput):
    self.sio.emit('digital_input_changed', dinput, namespace='/msgbus')

  def temperature_changed(self, temperature):
    self.sio.emit('temperature_changed', temperature, namespace='/msgbus')

  def state_changed(self, state):
    self.sio.emit('state_changed', state, namespace='/msgbus')