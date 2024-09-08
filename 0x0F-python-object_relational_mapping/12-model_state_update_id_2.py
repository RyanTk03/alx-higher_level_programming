#!/usr/bin/python3
"""
A script that changes the name of a State object from the given database.
"""
import sys
import sqlalchemy
from model_state import Base, State


if __name__ == '__main__':
    dbuser = sys.argv[1]
    dbpwd = sys.argv[2]
    dbname = sys.argv[3]

    engine = sqlalchemy.create_engine('mysql+mysqldb://{}:{}/localhost/{}'
                                      .format(dbuser, dbpwd, dbname))
    Base.metadata.create_all(engine)
    session = sqlalchemy.orm.Session(engine)

    state = session.query(State).filter(State.id == 2)
    state.name = 'New Mexico'

    session.commit()
    session.close()
