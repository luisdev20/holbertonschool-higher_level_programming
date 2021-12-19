#!/usr/bin/python3
"""This file contains the class definition of a State and an instance"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base


class City(Base):
    """
    Represents a column of a table for a MySQL database.

    id (Integer): The state's id
    name (String): The state's name
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
