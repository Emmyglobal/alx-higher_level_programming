#!/usr/bin/env python3
""" prints the first state object from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ collect the CLI arguments """
    uname = sys.argv[1]
    pword = sys.argv[2]
    dbase = sys.argv[3]

    """ create connection engine """
    engine = create_engine(
            f"mysql+mysqldb://{uname}:{pword}@localhost:3306/{dbase}",
            pool_pre_ping=True
            )

    """ Bind engine to session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query all states ordered by id """
    state = session.query(State).order_by(State.id).first()

    """ print out """
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    session.close()
