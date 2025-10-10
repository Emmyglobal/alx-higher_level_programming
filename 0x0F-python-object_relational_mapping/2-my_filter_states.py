#!/usr/bin/env python3
"""
Takes argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """ access all the arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
            )

    cur = db.cursor()

    """ Execute SQL: displays according argument search """
    cur.execute(
            "SELECT * FROM states WHERE name = %s", (state_name,)
            )

    rows = cur.fetchall();

    for row in rows:
        print(row)

    cur.close()
    db.close()
