#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: states table name
        name: input name
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City',
                          cascade='all, delete-orphan', backref='State')
    else:
        name = ""

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def cities(self):
            """ getter for cities that returns list of
                city instances with state_id equal to current State.id
            """
            city_list = []
            for city_search in self.cities:
                if city_search.state_id == self.id:
                    city_list.append(city_search)
            return(city_list)
