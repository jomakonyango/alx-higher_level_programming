#!/usr/bin/python3
"""
model_state.py

Python file that contains the class definition of a State and an instance
Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class

    Inherits from Base Tips
    Links to the MySQL table states
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
