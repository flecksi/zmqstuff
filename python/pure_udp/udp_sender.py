import socket
import time

# params
UDP_IP			= "127.0.0.1"
UDP_SEND_PORT	= 1234

MSG_SEND_LEN	= 1024  # bytelength
dT_SEND			= 0.001 # in seconds
N_MSGS_TO_SEND  = 10000


print('''#### udp sender ####''')

msg = b"hallo welt\n"


send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
n = 0
t_start = time.time()
#while True:
for i in range(N_MSGS_TO_SEND):
	#t1 = time.perf_counter()
	send_socket.sendto(msg, (UDP_IP,UDP_SEND_PORT))
	n += 1
	#t2 = time.perf_counter()
	#dt_msec = (t2-t1) * 1000
	#print("1 cycle took %0.4f msec\n" % dt_msec)
	#t_sleep = max(0,dT_SEND - (t2-t1))
	#time.sleep(t_sleep)
	time.sleep(dT_SEND)

t_end = time.time()
dt = t_end - t_start

print("sending %i messages took: %0.4f seconds" % (n,dt))
