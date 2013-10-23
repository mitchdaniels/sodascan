# Server program

from socket import *

import itemDatabase
import gaHits as ga

from generateID import generate_id

# Account-level GA parameters
version = '1'
trackingID = 'UA-44857140-1'
clientID = generate_id(5)
transactionID = generate_id(5)
transactionAffiliation = 'Falls Church'
itemQuantity = '1'


# Set the socket parameters
host = "localhost"
port = 21567
buf = 1024
addr = (host,port)

# Create socket and bind to address
UDPSock = socket(AF_INET,SOCK_DGRAM)
UDPSock.bind(addr)

# Receive messages
while 1:
	itemCode,addr = UDPSock.recvfrom(buf)
	if not itemCode:
		print "Client has exited!"
		break
	else:

		with itemDatabase.db:

			itemDatabase.cur.execute("SELECT * FROM items WHERE itemCode='" + itemCode + "'")

			while True:
				try:
					itemDetails = itemDatabase.cur.fetchall()[0]

					itemName 		= itemDetails[1]
					itemCategory 	= itemDetails[2]
					itemPrice 		= itemDetails[3]

					transactionRevenue = itemPrice

					ga.ga_transaction(version, trackingID, clientID, transactionID, transactionAffiliation, transactionRevenue)
					ga.ga_item(version, trackingID, clientID, transactionID, itemPrice, itemName, itemQuantity, itemCode, itemCategory)
					ga.ga_event(version, trackingID, clientID, itemCategory, itemName, itemCode)
					break

				except IndexError:
					print("Invalid Barcode. Please try again.")
					break

# Close socket
UDPSock.close()