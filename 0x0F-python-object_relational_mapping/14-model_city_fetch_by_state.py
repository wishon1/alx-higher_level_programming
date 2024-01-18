#!/usr/bin/python3
"""
Script that lists all City objects from the hbtn_0e_14_usa database.

Usage:
    ./14-model_city_fetch_by_state.py <mysql_username> <mysql_password>
    <database_name>

Arguments:
    mysql_username (str): MySQL username for database access.
    mysql_password (str): MySQL password for database access.
    database_name (str): Name of the database to connect to.

Note:
    This script connects to a MySQL server running on localhost at port 3306
    using the provided credentials and retrieves City objects from the
    'cities' table along with their associated State information.

Results are sorted in ascending order by cities.id and displayed in the
following format: <state name>: (<city id>) <city name>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
