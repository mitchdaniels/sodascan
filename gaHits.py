import requests

def ga_transaction(version, trackingID, clientID, transactionID, transactionAffiliation, transactionRevenue):

	payload = {
		# Required params
		'v': version,
		'tid': trackingID,
		'cid': clientID,
		't':'transaction', # Hit Type

		# Transaction Hit params
		'ti': transactionID, #(REQUIRED for transaction hits)
		'ta': transactionAffiliation,
		'tr': transactionRevenue}

	r = requests.post("http://www.google-analytics.com/collect",params=payload)
	print("Sent transaction") #r.url to see full request

def ga_item(version, trackingID, clientID, transactionID, itemPrice, itemName, itemQuantity, itemCode, itemCategory):

	payload = {
		# Required params
		'v': version,
		'tid': trackingID,
		'cid': clientID,
		't':'item', # Hit Type

		# Item Hit params
		'ti': transactionID, #(REQUIRED for item hits)
		'ip': itemPrice,
		'in': itemName,
		'iq': itemQuantity,
		'ic': itemCode,
		'iv': itemCategory}

	r = requests.post("http://www.google-analytics.com/collect",params=payload)
	print("Sent item")


#def GAPageview():

def ga_event(version, trackingID, clientID, eventCategory, eventAction, eventLabel):

	payload = {
		# Required params
		'v': version, # protocol version (always 1)
		'tid': trackingID,
		'cid': clientID,
		't':'event', # Hit Type

		# E-commerce params
		'ec': eventCategory,
		'ea': eventAction,
		'el': eventLabel}

	r = requests.post("http://www.google-analytics.com/collect",params=payload)
	print("Sent event")