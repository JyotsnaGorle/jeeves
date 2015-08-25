#!/usr/bin/env python

from __future__ import print_function          # maintain compatibility with Py3/Py3k
from twisted.internet import reactor, protocol

import sys, os

class Julius_Connection(protocol.Protocol):
    """
        Base Twisted reactor class for TCP connection to Julius-Core
         - Implements callbacks for connection made/loss and data received

        TODO:
         - Appened chunked data to form complete response from Julius-Core
         - Parse the response XML to for a senetence
    """
    def connectionMade(self):
        print("Connected to Julius-Core!")

    def dataReceived(self, data):
        print("Julius said:", data)

    def connectionLost(self, reason):
        print("Connection lost to Julius-Core!")

class Julius_Connect_Factory(protocol.ClientFactory):
    """
        Twisted Reactor factory for the reactor class
         - Implements the TCP connection to connect to Julius-Core
         - Stops when connection is reset by peer

         TODO:
          - Possibly have a connection timeout?
          - Try to reconnect on failure or termination?
    """
    protocol = Julius_Connection

    def clientConnectionFailed(self, connector, reason):
        self.halt("failed")

    def clientConnectionLost(self, connector, reason):
        self.halt("lost")

    def halt(self, status):
        print("Connection %s - exiting..." % status)
        reactor.stop()
        print("Exited!")

if len(sys.argv) != 3:
    sys.stderr.write("Invalid parameters, Usage: %s <server_ip> <server_port>%s" % (sys.argv[0], os.linesep))
    exit(1)

factory = Julius_Connect_Factory()
reactor.connectTCP(sys.argv[1], int(sys.argv[2]), factory)
reactor.run()
