#!/usr/bin/python3
"""This script lists all states with a name starting with N (upper N)"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = """SELECT id, c.name, s.name FROM states AS s
                JOIN cities AS c
                ON c.state_id = s.id
                ORDER BY c.id ASC"""
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
