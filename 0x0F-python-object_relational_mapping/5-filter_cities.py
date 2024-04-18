#!/usr/bin/python3
"""
5-filter_cities.py

Script that lists all cities from the database hbtn_0e_4_usa where state matches
the argument, safe from MySQL injections.
"""

import MySQLdb
import sys


def list_cities():
    """
    Lists all cities from the database hbtn_0e_4_usa where state matches the
    argument, safe from MySQL injections.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s ORDER BY cities.id ASC",
                (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join(city[1] for city in rows))
    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities()
