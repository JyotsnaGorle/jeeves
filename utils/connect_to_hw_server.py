from websocket import create_connection

ip = '192.168.0.176'
port = 5000

def connect_to_hw_server(control_device):
    ws = create_connection("ws://%s:%d" % (ip, port))
    ws.send(control_device)
    ws.close()
