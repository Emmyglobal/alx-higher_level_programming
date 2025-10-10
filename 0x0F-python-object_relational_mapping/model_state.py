#!/usr/bin/env python3
"""
Defines Base and State (SQLAlchemy declarative) and creates the table(s)
on a MySQL server running on localhost:3306.
"""

import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import OperationalError

"""this is the Base"""
Base = declarative_base()

class State(Base):
    """SQLAlchemy model for the 'states' table."""
    __tablename__ = "states"

    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement=True
            )
    name = Column(String(128), nullable=False)

"""if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"

    try:
        engine = create_engine(engine_url, echo=False)
        Base.metadata.create_all(engine)
        print("Tables created/verified successfully")
    except OperationalError as e:
        print("OperationalError (could not connect/create):", e)
        sys.exit(1)"""
