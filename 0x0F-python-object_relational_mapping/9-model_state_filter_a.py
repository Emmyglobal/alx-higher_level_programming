#!/usr/bin/env python3
"""lists all State objects that contain letter a from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Collect all CLI arguments """
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

    """ query all State with letter a """
    state = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for i in state:
        print(f"{i.id}: {i.name}")

    """ Close the session """
    session.close()

