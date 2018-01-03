import zmq
import time

print('''#### pyzmq proxy #####''')

## parameters
SUB_PORT     = 1234
PUB_PORT     = 1235

context = zmq.Context()

SUB_socket = context.socket(zmq.XSUB)
SUB_socket.bind("tcp://127.0.0.1:1234")

PUB_socket = context.socket(zmq.XPUB)
PUB_socket.bind("tcp://127.0.0.1:1235")

zmq.proxy(SUB_socket,PUB_socket)

SUB_socket.close()
PUB_socket.close()
context.term()
