#!/usr/bin/python3
"""
14-model_city_fetch_by_state.py

Script that prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def list_all_cities():
    """
    Prints all City objects from the database hbtn_0e_14_usa.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City).join(State).order_by(City.id):
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
    session.close()


if __name__ == "__main__":
    list_all_cities()
