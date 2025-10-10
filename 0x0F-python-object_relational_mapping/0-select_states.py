#!/usr/bin/env python3
"""
Lists all states from database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL username, password, and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server on localhost:3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor to execute queries
    cur = db.cursor()

    # Execute SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
