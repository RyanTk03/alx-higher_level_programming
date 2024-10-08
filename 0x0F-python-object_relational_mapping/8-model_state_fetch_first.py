#!/usr/bin/python3
"""
Prints the first State object from the given database.
"""
import sys
import sqlalchemy
from model_state import Base, State


if __name__ == '__main__':
    dbuser = sys.argv[1]
    dbpwd = sys.argv[2]
    dbname = sys.argv[3]
    engine = sqlalchemy.create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(dbuser, dbpwd, dbname))
    Base.metadata.create_all(engine)
    session = sqlalchemy.orm.Session(engine)

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print('Nothing')
    else:
        print('{}: {}'.format(state.id, state.name))

    session.close()
