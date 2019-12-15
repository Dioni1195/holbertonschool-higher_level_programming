#!/usr/bin/python3
""" This module lists all cities from a database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %(state)s\
                ORDER BY cities.id", {'state': argv[4]})
    cities = cur.fetchall()
    city_list = []
    for city in cities:
        city_list.append(city[0])
    str_new = ", ".join(city_list)
    print(str_new)
    cur.close()
    db.close()
