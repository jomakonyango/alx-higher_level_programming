#!/usr/bin/python3
"""
1-filter_states.py

Script that lists all states with a name starting with N from the database
hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states():
    """
    Lists all states with a name starting with N from the database
    hbtn_0e_0_usa.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = ("SELECT * FROM states "
             "WHERE name LIKE BINARY 'N%' "
             "ORDER BY id ASC")
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
