#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the given database.
"""
import MySQLdb
import sys


if __name__ == '__main__':
    dbuser = sys.argv[1]
    dbpwd = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=dbuser,
                         passwd=dbpwd, db=dbname)

    cursor = db.cursor()

    cursor.execute("""SELECT c.name FROM cities c JOIN states s ON c.state_id
                   = s.id AND s.name = %s ORDER BY c.id ASC""", (state_name,))

    results = cursor.fetchall()
    for i in range(len(results)):
        if i > 0:
            print(', ', end='')
        print(results[i][0], end='')

    print()
    cursor.close()
    db.close()
