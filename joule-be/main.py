#!/usr/bin/python
import time
from sockets.ws_cgi import wscgi

if __name__ == '__main__':
  print "hello!"
  ws = wscgi()

  while True:
    time.sleep(100)

