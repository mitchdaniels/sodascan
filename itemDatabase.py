import csv
import sqlite3
import os

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

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'items.csv')

populate_db(cur, open(filename,'rU'))
db.commit()