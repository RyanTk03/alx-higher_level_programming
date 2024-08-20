#!/usr/bin/python3
"""
A script that prints the State object with the name passed as argument from
the given database
"""
import sys
import sqlalchemy
from model_state import Base, State


if __name__ == '__main__':
    dbuser = sys.argv[1]
    dbpwd = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    engine = sqlalchemy.create_engine('mysql+mysqldb://{}:{}/localhost/{}'
                                      .format(dbuser, dbpwd, dbname))
    Base.metadata.create_all(engine)
    session = sqlalchemy.orm.Session(engine)

    results = session.query(State).filter(State.name == state_name)

    if len(results) == 0:
        print('Not found')
    else:
        for state in results:
            print(state.id)

    session.close()
