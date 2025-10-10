#!/usr/bin/env python3
""" list all State objects from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Collect CLI arguments"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
            pool_pre_ping=True
            )

    """Create a Session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Fetch the first state (ordered by id)"""
    states = session.query(State).order_by(State.id).all()

    """Display the result"""
    for state in states:
        print(f"{state.id}: {state.name}")

        """close session"""
        session.close()
