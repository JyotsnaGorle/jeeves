from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
from twisted.internet import reactor
from segregator.segregator import Segregator


class WebkitVoiceRecognizer(WebSocketServerProtocol):
    def __init__(self):
        self.is_speaking = False
        self.is_closed = False

    def onConnect(self, request):
        self.is_closed = False

    def onMessage(self, payload, is_binary):
        if not self.is_speaking:
            self.is_speaking = True
            segregator = Segregator(payload.decode('utf8'))
            segregator.segregate_and_react()
            self.is_speaking = False

    def onClose(self, was_clean, code, reason):
        self.is_closed = True

def recognize():
    factory = WebSocketServerFactory("ws://localhost:3002", debug=False)
    factory.protocol = WebkitVoiceRecognizer

    reactor.listenTCP(3002, factory)
    reactor.run()
