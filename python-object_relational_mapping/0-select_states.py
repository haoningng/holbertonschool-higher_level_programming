#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


db = MySQLdb.connect(user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT id, name FROM states")
rows = cur.fetchall()
for row in rows:
    print("({}, '{}')".format(row[0] + 1, row[1]))
cur.close()
db.close()
