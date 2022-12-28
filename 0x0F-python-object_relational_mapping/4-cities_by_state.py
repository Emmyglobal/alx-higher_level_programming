#!/usr/bin/python3
"""
Script that Lists all cities from the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    db_query = "SELECT cities.id, cities.name, states.name\
             FROM cities JOIN states\
             WHERE cities.state_id = states.id"
    cursor.execute(db_query)

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
