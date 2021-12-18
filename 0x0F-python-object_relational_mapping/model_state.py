#!/usr/bin/python3
"""This file contains the class definition of a State and an instance"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a column of a table for a MySQL database.

    id (Integer): The state's id
    name (String): The state's name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
