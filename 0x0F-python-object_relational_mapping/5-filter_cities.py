#!/usr/bin/env python3
""" takes in the name of a state as an argument and lists all cities"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    """ connect to the database """
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            db=database_name,
            passwd=password
            )

    cur = db.cursor()

    """ Execute SQL """
    cur.execute(
            """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """, (state_name,)
            )

    rows = cur.fetchall()

    for row in rows:
        print(row[0])

    cur.close()
    db.close()
