def protocol_init(sio):

    @sio.on('connect', namespace='/msgbus')
    def test_connect(sid, environ):
        sio.emit('connected', room=sid, namespace='/msgbus')

    @sio.on('pinging', namespace='/msgbus')
    def test_message(sid, message):
        sio.emit('msg', message, room=sid, namespace='/msgbus')