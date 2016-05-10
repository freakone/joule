import hal.maps.digital_outputs_map as do_map
import json

def protocol_init(sio, actions):
    @sio.on('connect', namespace='/msgbus')
    def test_connect(sid, environ):
        sio.emit('connected', room=sid, namespace='/msgbus')
        sio.emit('init', actions.digital_outputs.map, room=sid, namespace='/msgbus')

    @sio.on('set_digital', namespace='/msgbus')
    def test_message(sid, data):
        actions.set_output(data['id'], data['value'])
