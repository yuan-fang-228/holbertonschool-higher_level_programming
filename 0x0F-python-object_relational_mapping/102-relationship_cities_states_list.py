#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_101_usa"""
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
    citiesRows = session.query(City).join(State)\
        .filter(City.state_id == State.id).order_by(City.id)
    for cityRow in citiesRows:
        print(f"{cityRow.id}: {cityRow.name} -> {cityRow.state.name}")
    session.close()
