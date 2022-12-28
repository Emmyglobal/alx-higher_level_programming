#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db.cursor()

    query = "SELECT cities.name\
             FROM cities JOIN states\
             ON cities.state_id = states.id\
             WHERE states.name = %s"

    db_cursor.execute(query, (argv[4], ))
    cities = []
    for city in db_cursor.fetchall():
        cities.append(city[0])
    print(", ".join(cities))
    db_cursor.close()
    db.close()
