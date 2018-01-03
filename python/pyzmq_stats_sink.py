import zmq
import time

print('''#### pyzmq stats sink ####''')

## parameters
N_MSG_PLOT     = 1000 # print one line after a certain amount of msgs received

context = zmq.Context()

SUB_socket = context.socket(zmq.SUB)
SUB_socket.connect("tcp://127.0.0.1:1235")
SUB_socket.setsockopt_string(zmq.SUBSCRIBE, "") # subscribe to all msgs (no filter)

T_last_plot	= 0
n_msgs		= 0
bytes_msgs	= 0

while True:
	sub_msg = SUB_socket.recv() # blocking call
	n_msgs += 1
	bytes_msgs += len(sub_msg)
	if n_msgs > N_MSG_PLOT:
		dT = time.time() - T_last_plot
		n_msgs_per_sec = n_msgs / dT
		kbytes_per_sec = bytes_msgs / dT / 1024
		bytes_per_msg  = kbytes_per_sec / n_msgs_per_sec * 1024
		print("STATS: %0.2f msg/s \t(%0.2f KByte/s) \t %0.2f byte/msg " % (n_msgs_per_sec,kbytes_per_sec,bytes_per_msg))
		n_msgs = 0
		bytes_msgs = 0
		T_last_plot = time.time()
