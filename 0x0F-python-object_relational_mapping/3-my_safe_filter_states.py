#!/usr/bin/env python3
"""
a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument. But
this time, write one that is safe from MySQL injections!
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """Get data from the arguments passed"""
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=name
            )

    cur = db.cursor()

    """ Execute SQL command """
    cur.execute(
            "SELECT * FROM states WHERE name = %s", (state_name,)
            )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
