#!/usr/bin/python3
""" script that lists all State objects from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # connect with the db using create_engine() and create a session.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                            argv[2], argv[3]))
    session = sessionmaker(bind=engine)
    instance_session = session()

    for state in instance_session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
