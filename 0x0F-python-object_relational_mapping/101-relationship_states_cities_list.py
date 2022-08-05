#!/usr/bin/python3
"""list all States, and corresponding City, contained in the database"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    statesRows = session.query(State).order_by(State.id)
    for stateRow in statesRows:
        print(f"{stateRow.id}: {stateRow.name}")
        for city in stateRow.cities:
            print(f"    {city.id}: {city.name}")
    session.close()
