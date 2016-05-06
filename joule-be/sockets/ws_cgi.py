import asyncio
import protocol
from autobahn.asyncio.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory

class wscgi:
  def __init__(self):


  def start_server(self):
    factory = WebSocketServerFactory(u"ws://127.0.0.1:9000")
    factory.protocol = protocol.JouleProtocol

    loop = asyncio.get_event_loop()
    coro = loop.create_server(factory, '0.0.0.0', 9000)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.close()