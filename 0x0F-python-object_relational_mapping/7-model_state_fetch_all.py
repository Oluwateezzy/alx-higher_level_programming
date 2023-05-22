#!/usr/bin/python3

'''
    Lists all state objs.
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

user = sys.argv[1]
sql = sys.argv[2]
db = sys.argv[3]

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(user, sql, db))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).order_by(State.id).all()

for state in states:
    print(f"{state.id}: {state.name}")

session.close()
