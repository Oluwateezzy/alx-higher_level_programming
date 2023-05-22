#!/usr/bin/python3

'''
    Lists all state objs.
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    sql = sys.argv[2]
    db = sys.argv[3]
    st = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, sql, db))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)\
                    .filter(State.name.like(st))\
                    .first()
    session.close()
    engine.dispose()

    if states:
        print(states.id)
    else:
        print("Not found")
