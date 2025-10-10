#!/usr/bin/python3
"""prints State object with the name passed as arg from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """collect cli arguments"""
    uname = sys.argv[1]
    pword = sys.argv[2]
    dbase = sys.argv[3]
    npasd = sys.argv[4]

    """ create connection engine """
    engine = create_engine(
            f"mysql+mysqldb://{uname}:{pword}@localhost:3306/{dbase}",
            pool_pre_ping=True
            )

    """ create a configured session class """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query all State objects with name passed as argument """
    state = session.query(State).filter(State.name.like(f'%{npasd}%')).order_by(State.id).all()

    """ Display result """
    if state:
        for i in state:
            print(f"{i.id}")
    else:
        print("Not found")

    """ Close session """
    session.close()
