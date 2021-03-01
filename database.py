#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

def show_all():
    '''
    Creates, executes DB and shows everything in it
    '''
    
    conn = sqlite3.connect('customer.dt') 
    c = conn.cursor()
    
    c.execute("SELECT rowid, * FROM customers ORDER BY first_name")

    items = c.fetchall()
    
    for item in items:
        print(item)

    conn.commit()
    conn.close()


def add_one(first_name, last_name, email):
    '''
    Adds one customer with properties: "first name"(str), "last name"(str) and "email"(str)
    '''
    conn = sqlite3.connect('customer.dt') 
    c = conn.cursor()

    customer = [first_name, last_name, email]

    c.execute("INSERT INTO customers VALUES (?,?,?)", customer)

    for item in customer:
        print("Customer", item[0], item[1],  "is added")

    conn.commit()
    conn.close()


def add_many(array):
    '''
    '''
    conn = sqlite3.connect('customer.dt') 
    c = conn.cursor()


    c.executemany("INSERT INTO customers VALUES (?,?,?)", array)

    for item in array:
        print("Customer", item[0], item[1],  "is added")

    conn.commit()
    conn.close()


def delete_one(key, item):
    '''
    Delete a customer from DB by a category "key"(str) with its "item"(str) 
    "key" = rowid, first_name, last_name, email
    "item" = a concret item 
    example: key = "first_name", item = "Mary"
    '''

    conn = sqlite3.connect('customer.dt') 
    c = conn.cursor()

    c.execute('''
    DELETE from customers WHERE {} = {}
    '''.format(key, item))

    conn.commit()
    conn.close()