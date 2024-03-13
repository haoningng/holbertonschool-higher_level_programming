#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa"""
import MySQLdb


db = MySQLdb.connect(host="localhost", port=3306, user="root",
                     passwd="root", db="hbtn_0e_0_usa")
cur = db.cursor()
cur.execute("SELECT id, name FROM states")
rows = cur.fetchall()
for row in rows:
    print("({}, '{}')".format(row[0] + 1, row[1]))
