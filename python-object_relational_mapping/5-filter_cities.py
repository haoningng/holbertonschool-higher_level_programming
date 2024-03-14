#!/usr/bin/python3
"""This script lists all cities of that state, using the database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = """SELECT c.name FROM states AS s
                JOIN cities AS c
                ON c.state_id = s.id
                WHERE s.name = %s
                ORDER BY c.id ASC"""
    state = sys.argv[4]
    cur.execute(query, (state, ))
    rows = cur.fetchall()
    num = 0
    for row in rows:
        if num == 0:
            print(row[0], end="")
            num += 1
        else:
            print(', ' + row[0], end="")
            num += 1
    print()
    cur.close()
    db.close()
