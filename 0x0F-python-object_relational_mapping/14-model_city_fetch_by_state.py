#!/usr/bin/python3

'''
    Lists all state objs.
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    user = sys.argv[1]
    sql = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, sql, db))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State, City).\
        filter(State.id == City.state_id).order_by(City.id).all()
    for state, city in rows:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
