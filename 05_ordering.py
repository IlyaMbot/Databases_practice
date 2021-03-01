#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3


# create a database
conn = sqlite3.connect('customer.dt') 

# create a cursor
c = conn.cursor()

# order ASC | DESC
c.execute("SELECT rowid, * FROM customers ORDER BY first_name")

customer_f = c.fetchall()
for item in customer_f:
    print(item[0], item[1], item[2], 'is found')

conn.commit()


#close the connection
conn.close()
