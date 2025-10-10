#!/usr/bin/env python3
""" A script that lists all cities from the database hbtn_0e_4_usa """

import sys
import MySQLdb

if __name__ == "__main__":
    """ Access all input arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]

    """connect to MySQLdb database"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=name
            )

    """ cursor """
    cur = db.cursor()

    """Execute SQL commands """
    cur.execute(
            "SELECT id, name FROM cities ORDER BY id ASC"
            )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
