#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Flaot
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        __tablename__: amenity table name
        name: input name
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)

    place_amenities = relationship(
                      "Place", backref="Amenity", cascade="all, delete-orphan")
