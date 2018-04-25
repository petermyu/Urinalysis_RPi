import os
import glob
import time
import RPi.GPIO as GPIO
from bluetooth import *

#while True:
#	print(read_temp())	
#	time.sleep(1)

def send_bt_data(value):
	server_sock=BluetoothSocket( RFCOMM )
	server_sock.bind(("",PORT_ANY))
	server_sock.listen(1)

	port = server_sock.getsockname()[1]

	uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

	advertise_service( server_sock, "UrinalysisServer",
					   service_id = uuid,
					   service_classes = [ uuid, SERIAL_PORT_CLASS ],
					   profiles = [ SERIAL_PORT_PROFILE ], 
	#                   protocols = [ OBEX_UUID ] 
						)
	while True:
		print "Waiting for connection on RFCOMM channel %d" % port

		client_sock, client_info = server_sock.accept()
		print "Accepted connection from ", client_info

		try:
				data = client_sock.recv(1024)
				if len(data) == 0: break
				print "received [%s]" % data

			msg = str(value) + ';'
			client_sock.send(msg)
			print "sending [%s]" % msg

		except IOError:
			pass

		except KeyboardInterrupt:

			print "disconnected"

			client_sock.close()
			server_sock.close()
			print "all done"

			break
