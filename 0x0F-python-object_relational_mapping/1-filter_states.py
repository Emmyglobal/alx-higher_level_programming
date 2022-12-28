#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db.cursor()

    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
             ORDER BY states.id ASC")

    for state in db_cursor.fetchall():
        print(state)
    db_cursor.close()
    db.close()
