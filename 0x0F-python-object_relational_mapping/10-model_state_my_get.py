#!/usr/bin/python3
"""
10-model_state_my_get.py

Script that prints the State object with the name passed as argument from the
database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_state_by_name():
    """
    Prints the State object with the name passed as argument from the
    database hbtn_0e_6_usa.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)
    session.close()


if __name__ == "__main__":
    fetch_state_by_name()
