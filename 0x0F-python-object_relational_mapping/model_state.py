#!/usr/bin/python3
""" Defines a City model.
    +Inherits from SQLAlchemy Base and links to the MySQL table cities.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Represents a city entity linked to the MySQL table 'cities'.

    Attributes:
        id (int): Represents a unique, auto-generated integer serving as the
                  primary key. Cannot be null.
        name (str): Represents a str of up to 128 characters. Can't be null.
        state_id (int): Represents an int serving as a foreign key to the
                        'states' table. Cannot be null.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
