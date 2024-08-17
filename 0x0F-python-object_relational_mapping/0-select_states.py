#!/usr/bin/python3
"""Script that lists all states from a given database."""
import MySQLdb
import sys


if __name__ == '__main__':
    dbuser = sys.argv[1]
    dbpwd = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=dbuser,
                         passwd=dbpwd, db=dbname)

    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id ASC')

    for record in cursor.fetchall():
        print(record)

    cursor.close()
    db.close()
