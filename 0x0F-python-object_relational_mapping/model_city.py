#!/usr/bin/python3

'''
    Python file that contains the class definition of a
    State and an instance Base = declarative_base()
'''
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
        city class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
