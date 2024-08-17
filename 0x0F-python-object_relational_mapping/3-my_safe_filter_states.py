#!/usr/bin/python3
"""
A safe version of the script that takes in an argument and displays all values
in the states table of a given database where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == '__main__':
    dbuser = sys.argv[1]
    dbpwd = sys.argv[2]
    dbname = sys.argv[3]
    state_searched = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=dbuser,
                         passwd=dbpwd, db=dbname)

    cursor = db.cursor()

    cursor.execute('SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC',
                   (state_searched,))

    for record in cursor.fetchall():
        print(record)

    cursor.close()
    db.close()
