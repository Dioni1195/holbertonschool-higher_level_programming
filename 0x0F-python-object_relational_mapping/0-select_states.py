#!/usr/bin/python3
""" This module lists all states from a database"""
import MySQLdb
from sys import argv

host = "127.0.0.1"
my_db = MySQLdb.connect(host=host, user=argv[1], passwd=argv[2], db=argv[3])
cur = my_db.cursor()
cur.execute("SELECT id, name FROM states")
states = cur.fetchall()
for state in states:
    print (state)
