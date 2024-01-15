#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # connect to db using create_engine() and interact with db using
    # +sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    instance_session = Session()

    # Query and filter states
    states = instance_session.query(State).order_by(State.id)

    for state in states:
        if state.id == 2:
            state.name = "New Mexico"
            break

    instance_session.commit()
    instance_session.close()
