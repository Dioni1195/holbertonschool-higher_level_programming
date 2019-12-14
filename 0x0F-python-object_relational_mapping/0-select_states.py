#!/usr/bin/python3
""" This module lists all states from a database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    ht = "127.0.0.1"
    db = MySQLdb.connect(host=ht, user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
