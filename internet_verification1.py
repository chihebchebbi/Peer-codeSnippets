#!/usr/bin/env python


import socket
REMOTE_SERVER = "www.tek-up.de"
def is_connected():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return "Internet"
  except:
     pass
     return False
print is_connected()
