#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3


# create a database
conn = sqlite3.connect('customer.dt') 

# create a cursor
c = conn.cursor()

"""
# changes the item where another item is *(rowid, lats_name, ...)
c.execute('''
    UPDATE customers SET first_name = "David"
    WHERE rowid = "5"
    ''')
"""

# deletes names
c.execute('''
    DELETE from customers WHERE rowid = "6"
    ''')


conn.commit()

c.execute("SELECT rowid, * FROM customers ")

customer_f = c.fetchall()
for item in customer_f:
    print(item[0], item[1], item[2], 'is found')

conn.commit()


#close the connection
conn.close()
