from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
from twisted.internet import reactor

import RPi.GPIO as GPIO

hw_pin_layout = {
    "fan": 18,
    "charger": 16,
    "coffee_machine": 12
}

switch_modes = {
    "on": False,
    "off": True
}


class HWRouter(WebSocketServerProtocol):
    def onConnect(self, request):
        print("Client connected")

    def onMessage(self, payload, isBinary):
        message = payload.decode('utf8').split(":")
        action, device = message[0], message[1]

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(hw_pin_layout[message[1]], GPIO.OUT)
        GPIO.output(hw_pin_layout[message[1]], switch_modes[action])

    def onClose(self, wasClean, code, reason):
        print("Connection closed")


factory = WebSocketServerFactory("ws://localhost:5000", debug=False)
factory.protocol = HWRouter

reactor.listenTCP(5000, factory)
reactor.run()
