#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import os
import models
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: states table name
        name: input name
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
                'City', cascade='all, delete-orphan', backref='state')

    else:
        @property
        def cities(self):
            """ getter for cities that returns list of
                city instances with state_id equal to current State.id
            """
            city_list = []
            for city_search in models.storage.all(City).values():
                if city_search.state_id == self.id:
                    city_list.append(city_search)
            print(city_list)
            return(city_list)
