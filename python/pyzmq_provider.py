import time
import zmq

print('''#### pyzmq data provider ####''')

context = zmq.Context()

PUB_socket = context = context.socket(zmq.PUB)
PUB_socket.connect("tcp://localhost:1234")

while True:
	PUB_socket.send(b"SIG1 1234")
	time.sleep(0.001)
