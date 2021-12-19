#!/usr/bin/python3
"""deletes all State objects with a name containing the letter 'a'
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for cities, states in session.query(City, State)\
                                 .filter(City.state_id == State.id)\
                                 .order_by(City.id):
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
