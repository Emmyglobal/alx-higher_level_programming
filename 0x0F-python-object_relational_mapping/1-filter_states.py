#!/usr/bin/env python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """ Select all input arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    cur = db.cursor()

    """ Execute SQL query: names starting with 'N'"""
    cur.execute(
    "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
