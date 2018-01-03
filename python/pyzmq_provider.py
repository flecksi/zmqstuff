import time
import zmq

#params
DATA_SIZE_BYTES = 1024 

print('''#### pyzmq data provider ####''')

context = zmq.Context()

PUB_socket = context = context.socket(zmq.PUB)
PUB_socket.connect("tcp://127.0.0.1:1234")

data = "SIG1 "
for i in range(DATA_SIZE_BYTES - len(data)):
	data += "1"

print("Data size = %i" % len(data))

while True:
	#PUB_socket.send(b"SIG1 1234")
	PUB_socket.send_string(data)
	time.sleep(0.001)
