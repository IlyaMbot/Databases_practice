#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

#saves the DB?
#conn = sqlite3.connect(':memory')

# create a database
conn = sqlite3.connect('customer.dt') 

# create a cursor
c = conn.cursor()

# searches for the particular "name" in the item "last_name"
#c.execute("SELECT rowid, * FROM customers WHERE last_name = 'More'")

# searches for the particular "name" in the item "last_name"
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'M%'")

customer_f = c.fetchall()
for item in customer_f:
    print(item[0], item[1], item[2], 'is found')



#commit the command
conn.commit()

#close the connection
conn.close()
