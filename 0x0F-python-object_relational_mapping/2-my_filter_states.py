#!/usr/bin/python3
"""
2-my_filter_states.py

Script that lists all states from the database hbtn_0e_0_usa where name matches
the argument.
"""

import MySQLdb
import sys


def list_states():
    """
    Lists all states from the database hbtn_0e_0_usa where name matches the
    argument.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
