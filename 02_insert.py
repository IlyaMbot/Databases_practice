#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# create a database
conn = sqlite3.connect('customer.dt') 

# create a cursor
c = conn.cursor()

# adds many customers' data
many_customers = [
    ('Carolina', 'Aslek', 'cutieaslek.com'),
    ('David', 'More', 'davidmore')
    ]


# add a customer
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
for cust in many_customers:
    print("Customer", cust[0], cust[1],  "is added")

#commit the command
conn.commit()

#close the connection
conn.close()
