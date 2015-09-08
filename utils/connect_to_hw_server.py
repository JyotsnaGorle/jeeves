from websocket import create_connection

ip = '10.136.125.217'
port = 5000

def connect_to_hw_server(control_device):
    ws = create_connection("ws://%s:%d" % (ip, port))
    ws.send(control_device)
    ws.close()
