#!/usr/bin/python3
'''filter all state in database'''

import MySQLdb
import sys


def listall():
    '''list all'''
    user = sys.argv[1]
    pas = sys.argv[2]
    db = sys.argv[3]
    state = sys.argv[4]

    connect = MySQLdb.connect(host='localhost', port=3306,
                              user=user, passwd=pas, db=db)
    cursor = connect.cursor()
    cursor.execute('SELECT c.name FROM cities c INNER JOIN states s ' +
                   'ON s.id = c.state_id WHERE ' +
                   'BINARY s.name = %s ' +
                   'ORDER BY c.id ASC;', [state])
    rows = cursor.fetchall()
    cursor.close()
    connect.close()
    print(', '.join(map(lambda x: x[0], rows)))


if __name__ == '__main__':
    listall()
