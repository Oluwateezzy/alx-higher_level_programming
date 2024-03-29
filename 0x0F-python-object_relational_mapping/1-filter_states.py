#!/usr/bin/python3
'''filter all state in database'''

import MySQLdb
import sys


def listall():
    '''list all'''
    user = sys.argv[1]
    pas = sys.argv[2]
    db = sys.argv[3]

    connect = MySQLdb.connect(host='localhost', port=3306,
                              user=user, passwd=pas, db=db)
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC;')
    rows = cursor.fetchall()
    cursor.close()
    connect.close()
    for row in rows:
        if row[1][0] == "N":
            print(row)


if __name__ == '__main__':
    listall()
