#!/usr/bin/python3
"""
    Lists all State objects that contain the letter a
    from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # connect to db using create_engine() and interact with db using
    # +sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    instance_session = Session()

    # Query and filter states
    states = instance_session.query(State).order_by(State.id)

    for state in states:
        # Check if letter 'a' is in the state name
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))

    instance_session.close()
