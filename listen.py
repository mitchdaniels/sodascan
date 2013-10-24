import send

# Listen for itemCode input
while True:
	itemCode = raw_input("Enter Barcode: ")
	if itemCode:
		send.send_data(itemCode)