#!/usr/bin/python3
"""
Contains the class definition of a State and an instance of the Base class.
"""


import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Represents a state in the MySQL database."""

    __tablename__ = 'states'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True,
                           primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
