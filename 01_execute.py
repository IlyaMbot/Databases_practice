#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

#saves the DB?
#conn = sqlite3.connect(':memory')

# create a database
conn = sqlite3.connect('customer.dt') 

# create a cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
        )
    """)

#commit the command
conn.commit()

#close the connection
conn.close()
