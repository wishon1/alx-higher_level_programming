#!/usr/bin/python3
"""
Defines a City model.

Inherits from SQLAlchemy Base and links to the MySQL table 'cities'.

Note:
    The City model is designed for use in a MySQL database.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
        id (int): The city's unique identifier (primary key).
        name (str): The name of the city (up to 128 characters).
        state_id (int): The foreign key to the associated state's id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
