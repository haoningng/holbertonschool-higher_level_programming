#!/usr/bin/python3
"""This script lists all states with a name starting with N (upper N)"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = """SELECT id, name FROM states
                WHERE BINARY name = %s ORDER BY id ASC"""
    state = sys.argv[4]
    cur.execute(query, (state, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
