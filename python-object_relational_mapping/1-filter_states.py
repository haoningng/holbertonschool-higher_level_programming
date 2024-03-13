#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT id, name FROM states WHERE
                name like 'N%' ORDER BY id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
