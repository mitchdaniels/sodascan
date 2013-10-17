import itemDatabase
import scan
import gaHits as ga

def send_scan(itemCode):

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