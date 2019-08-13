#!/usr/bin/python3
''' database storage class for AirBnB
'''

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
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

        Base.metadata.create_all(self.__engine)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        '''queries on the current database session (self.__session)
        '''
        cls_dict = {}
        cls_list = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

        if cls is not None:
            for cls_inst in self.__session.query(models.classes[cls]).all():
                    for objects in cls_inst:
                        cls_dict.append(cls_inst)


        else:
            for all_class in cls_list:
                for cls_inst in self.__sesion.query(models.classes[all_class]).all():
                    cls_dict.append(cls_inst)
       # if cls is None:
        #    for cls_inst in self.__session.query(
         #       User, State, City, Amenity, Place, Review).all():
          #      cls_dict.append(cls_inst)

        return(cls_dict)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        for items_to_delete in obj:
            self.__session.delete(items_to_delete)

    def reload(self):
        Session = sessionmaker(bind=engine, expire_on_commit=False)
        session = scoped_session(Session)
