import csv
import sqlite3

db = sqlite3.connect(':memory:')

def init_db(cur):
    cur.execute('''CREATE TABLE items (
        itemCode TEXT,
        itemName TEXT,
        itemCategory TEXT,
        itemPrice REAL)''')

def populate_db(cur, csv_fp):
    rdr = csv.reader(csv_fp)
    cur.executemany('''
        INSERT INTO items (itemCode, itemName, itemCategory, itemPrice)
        VALUES (?,?,?,?)''', rdr)

cur = db.cursor()
init_db(cur)
populate_db(cur, open('items.csv','rU'))
db.commit()