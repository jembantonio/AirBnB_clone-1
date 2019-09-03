#!/usr/bin/python3
''' database storage class for AirBnB
'''

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    '''Database Storage class
    '''
    __engine = None
    __session = None

    def __init__(self):
        ''' initializes the Database Storage instance
        '''
        user = os.getenv("HBNB_MYSQL_USER")
        pswd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        dbse = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user, pswd, host, dbse,
                                              pool_pre_ping=True))

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''queries on the current database session (self.__session)
        '''
        cls_dict = {}
        class_list = [State, City, User, Place, Review, Amenity]

        if cls is not None:
            for c_object in self.__session.query(eval(cls)).all():
                key = "{}.{}".format(type(c_object).__name__, c_object.id)
                cls_dict[key] = c_object

        else:
            for classes in class_list:
                for c_object in self.__session.query(classes).all():
                    key = "{}.{}".format(type(c_object).__name__, c_object.id)
                    cls_dict[key] = c_object

        return cls_dict

    def new(self, obj):
        if obj:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        self.__session.remove()
