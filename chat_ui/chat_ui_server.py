from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File
from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS

import ports


class BroadcastServerProtocol(WebSocketServerProtocol):
    def onOpen(self):
        self.factory.register(self)

    def onMessage(self, payload, isBinary):
        self.factory.broadcast(payload.decode('utf8'))

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)


class BroadcastServerFactory(WebSocketServerFactory):
    def __init__(self, url, debug=False, debugCodePaths=False):
        WebSocketServerFactory.__init__(self, url, debug=debug, debugCodePaths=debugCodePaths)
        self.clients = []

    def register(self, client):
        if client not in self.clients:
            self.clients.append(client)

    def unregister(self, client):
        if client in self.clients:
            self.clients.remove(client)

    def broadcast(self, msg):
        for client in self.clients:
            client.sendMessage(msg.encode('utf8'))


ServerFactory = BroadcastServerFactory

factory = ServerFactory("ws://127.0.0.1:%d" % ports.ports["chat_ui_server_ws_port"], debug=False, debugCodePaths=False)

factory.protocol = BroadcastServerProtocol
factory.setProtocolOptions(allowHixie76=True)
listenWS(factory)

web_root = File("chat_ui")
web = Site(web_root)
reactor.listenTCP(ports.ports["chat_ui_static_port"], web)

print("Chat UI Server is up at port %d" % ports.ports["chat_ui_static_port"])
reactor.run()
