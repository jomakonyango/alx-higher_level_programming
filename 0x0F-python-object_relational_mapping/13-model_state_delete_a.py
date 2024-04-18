#!/usr/bin/python3
"""
13-model_state_delete_a.py

Script that deletes all State objects with a name
containing the letter 'a' from
the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a():
    """
    Deletes all State objects with a name containing the letter 'a' from the
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
    for state in session.query(State).filter(State.name.contains('a')):
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    delete_states_with_a()
