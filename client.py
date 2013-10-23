# Client program
import subprocess
import atexit
import sys
from socket import *

#p = subprocess.Popen("python" + " server.py &", shell=True)

# Set the socket parameters
host = "localhost"
port = 21567
buf = 1024
addr = (host,port)

# Create socket
UDPSock = socket(AF_INET,SOCK_DGRAM)

def_msg = "===Enter message to send to server===";
print "\n",def_msg

try:
	while True:
		barcode = raw_input("Enter Barcode: ")
		if barcode:
			print "Sending Barcode: '",barcode,"'..."
			UDPSock.sendto(barcode, addr)
except KeyboardInterrupt:
	#Shutdown
	UDPSock.close()