#!/usr/bin/python3
"""
12-model_state_update_id_2.py

Script that changes the name of a State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state():
    """
    Changes the name of a State object from the database hbtn_0e_6_usa.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter_by(id=2).first()
    if state is not None:
        state.name = "New Mexico"
        session.commit()
    session.close()


if __name__ == "__main__":
    update_state()
