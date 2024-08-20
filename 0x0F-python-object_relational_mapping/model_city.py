#!/usr/bin/python3
"""
Contains the class definition of a City.
"""
import sqlalchemy
from model_state import Base, State


class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)

    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
    
    state_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey('states.id'),
                                 autoincrement=True, nullable=False)
