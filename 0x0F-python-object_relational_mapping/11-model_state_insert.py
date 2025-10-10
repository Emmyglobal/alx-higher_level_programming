#!/usr/bin/python3
""" adds the state object Louisiana to the database """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ collect all CLI arguments """
    uname = sys.argv[1]
    pword = sys.argv[2]
    dbase = sys.argv[3]

    """ Create connection engine """
    engine = create_engine(
            f"mysql+mysqldb://{uname}:{pword}@localhost:3306/{dbase}",
            pool_pre_ping=True
            )

    """ create a configured session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Adds the state object Louisiana to the database """
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    """ Display the id """
    print(f"{new_state.id}")

    session.close()
