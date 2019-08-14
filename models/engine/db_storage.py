#!/usr/bin/python3
''' database storage class for AirBnB
'''

import os
from sqlalchemy import create_engine
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

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pswd, host, dbse), pool_pre_ping=True)

        Base.metadata.bind = self.__engine

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''queries on the current database session (self.__session)
        '''
        cls_dict = {}
        cls_list = ['State', 'City']

        if cls is not None:
            for cls_inst in self.__session.query(eval(cls).all()):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                cls_dict[key] = obj

        else:
            for all_class in cls_list:
                for cls_inst in self.__session.query(all_class).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    cls_dict[key] = obj

       # if cls is None:
        #    for cls_inst in self.__session.query(
         #       User, State, City, Amenity, Place, Review).all():
          #      cls_dict.append(cls_inst)

        return(cls_dict)

    def new(self, obj):
        if obj:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
