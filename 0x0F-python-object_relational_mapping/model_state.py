#!/usr/bin/python3
"""Class definition of a State"""
import sqlalchemy
from sqlalchemy.orm import relationship


Base = sqlalchemy.ext.declarative.declarative_base()


class State(Base):
    """Class State"""

    __tablename__ = 'states'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True,
                           primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
