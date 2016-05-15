import hal.maps.digital_outputs_map as do_map
import json

def protocol_init(sio, actions):
    @sio.on('connect', namespace='/msgbus')
    def test_connect(sid, environ):
        sio.emit('connected', room=sid, namespace='/msgbus')
        sio.emit('digital_output_init', actions.digital_outputs.map, room=sid, namespace='/msgbus')
        sio.emit('jowenta_init', actions.jowenta.map, room=sid, namespace='/msgbus')
        sio.emit('digital_input_init', actions.digital_inputs.map, room=sid, namespace='/msgbus')
        sio.emit('temperature_init', actions.temperatures.map, room=sid, namespace='/msgbus')
        sio.emit('state_init', actions.state.state_map, room=sid, namespace='/msgbus')

    @sio.on('set_digital', namespace='/msgbus')
    def set_digital(sid, data):
        actions.set_output(data['id'], data['value'])

    @sio.on('set_name', namespace='/msgbus')
    def set_name(sid, name):
        actions.set_name(name)

    @sio.on('set_digital_output_name', namespace='/msgbus')
    def set_name(sid, data):
        actions.set_digital_output_name(data['id'], data['value'])

    @sio.on('set_jowenta_name', namespace='/msgbus')
    def set_name(sid, data):
        actions.set_jowenta_name(data['id'], data['value'])

    @sio.on('set_temperature_name', namespace='/msgbus')
    def set_name(sid, data):
        actions.set_temperature_name(data['id'], data['value'])

