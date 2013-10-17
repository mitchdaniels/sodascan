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

itemCode = raw_input("Product SKU: ")

with itemDatabase.db:

	itemDatabase.cur.execute("SELECT * FROM items WHERE itemCode='" + itemCode + "'")

	itemDetails = itemDatabase.cur.fetchall()[0]

	itemName 		= itemDetails[1]
	itemCategory 	= itemDetails[2]
	itemPrice 		= itemDetails[3]

	transactionRevenue = itemPrice

ga.ga_transaction(version, trackingID, clientID, transactionID, transactionAffiliation, transactionRevenue)
ga.ga_item(version, trackingID, clientID, transactionID, itemPrice, itemName, itemQuantity, itemCode, itemCategory)
ga.ga_event(version, trackingID, clientID, itemCategory, itemName, itemCode)