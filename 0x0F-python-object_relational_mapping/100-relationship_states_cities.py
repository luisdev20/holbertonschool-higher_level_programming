#!/usr/bin/python3
"""Creates the State “California” with the City “San Francisco"
   from the database hbtn_0e_100_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata_create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    san_francisco = City(name="San Francisco", state=State(name="California"))
    session.add(san_francisco)
    session.commit()
