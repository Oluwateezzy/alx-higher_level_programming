#!/usr/bin/env python3
'''lists all state in database'''
import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

connect = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user = username,
        passwd = password,
        db = database
)
cursor = connect.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC;")
rows = cursor.fetchall()
cursor.close()
connect.close()

for row in rows:
    print(row)
