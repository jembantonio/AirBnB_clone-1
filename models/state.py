#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Foreignkey
import sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: states table name
        name: input name
    """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City',
                              cascade='all, delete-orphan', backref='State')
    else:
        name = ""

    @property
    def cities(self):
        """ getter for cities that returns list of
            city instances with state_id equal to current State.id
        """
        city_list = []
        for city_search in models.storage.all('City').value():
            if city_search.state_id == self.id:
                city_list.append(city_search)
        return city_list
