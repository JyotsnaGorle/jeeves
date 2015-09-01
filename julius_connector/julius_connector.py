from __future__ import print_function          # maintain compatibility with Py3/Py3k
from twisted.internet import reactor, protocol
from HTMLParser import HTMLParser
from segregator.segregator import Segregator

sentence = []

class ResponseParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global sentence
        ignored = ["<s>", "</s>"]

        if tag == "whypo":
            word = attrs[0][1]

            if word not in ignored:
                sentence.append(word.lower())
        elif tag == "recogfail":
            sentence = []

parser = ResponseParser()

class JuliusConnection(protocol.Protocol):
    """
        Base Twisted reactor class for TCP connection to Julius-Core
         - Implements callbacks for connection made/loss and data received

        TODO:
         - Append chunked data to form complete response from Julius-Core
         - Parse the response XML to for a sentence
    """
    def __init__(self):
        self.full_xml = []

    def sanitize(self, what):
        return what.replace(".\n", "").replace("\n", "").replace(">.", ">")

    def send_to_jeeves(self, what):
        global sentence

        parser.feed(what)

        if len(sentence) > 0:
            # segregator = Segregator(' '.join(sentence))
            # segregator.segregate_and_react()

    def connectionMade(self):
        print("Connected to Julius-Core!")

    def dataReceived(self, data):
        for response in data.strip().split('\n.\n'):
            if '<INPUT STATUS="LISTEN"' in response:
                if len(self.full_xml) > 0:
                    self.send_to_jeeves(''.join(self.full_xml))
                    self.full_xml = []
            else:
                self.full_xml.append(self.sanitize(response))

    def connectionLost(self, reason):
        print("Connection lost to Julius-Core!")

class JuliusConnectFactory(protocol.ClientFactory):
    """
        Twisted Reactor factory for the reactor class
         - Implements the TCP connection to connect to Julius-Core
         - Stops when connection is reset by peer

         TODO:
          - Possibly have a connection timeout?
          - Try to reconnect on failure or termination?
    """
    protocol = JuliusConnection

    def clientConnectionFailed(self, connector, reason):
        self.halt("failed")

    def clientConnectionLost(self, connector, reason):
        self.halt("lost")

    def halt(self, status):
        print("Connection %s - exiting..." % status)
        reactor.stop()
        print("Exited!")

def connect_to_julius(host, port):
    factory = JuliusConnectFactory()
    reactor.connectTCP(host, port, factory)
    reactor.run()
