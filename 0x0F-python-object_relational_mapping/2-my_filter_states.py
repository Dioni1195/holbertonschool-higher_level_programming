#!/usr/bin/python3
""" This module lists all states that stars with N from a database"""
import MySQLdb
from sys import argv

host = "127.0.0.1"
my_db = MySQLdb.connect(host=host, user=argv[1], passwd=argv[2], db=argv[3])
cur = my_db.cursor()
cur.execute("SELECT id, name FROM states WHERE name = '{}'".format(argv[4]))
states = cur.fetchall()
for state in states:
    print(state)
