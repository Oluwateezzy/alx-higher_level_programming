#!/usr/bin/python3

'''
    Lists all state objs.
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.schema import Table

if __name__ == "__main__":
    user = sys.argv[1]
    sql = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, sql, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    rows = session.query(State).order_by(State.id).all()

    for state in rows:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
    session.close()
