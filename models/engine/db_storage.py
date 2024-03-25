#!/usr/bin/python3
"""
Defines DBStorage
"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import relationship


class DBStorage:
    """
    Represents a database storage engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        DBStorage instance
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        all objects
        """
        if cls is None:
            Objcts = self.__session.query(State).all()
            Objcts.extend(self.__session.query(City).all())
            Objcts.extend(self.__session.query(User).all())
            Objcts.extend(self.__session.query(Place).all())
            Objcts.extend(self.__session.query(Review).all())
            Objcts.extend(self.__session.query(Amenity).all())

        else:
            if type(cls) == str:
                cls = eval(cls)
            Objcts = self.__session.query(cls)

        return {"{}.{}".format(type(o).__name__, o.id): o for o in Objcts}

    def new(self, obj):
        """add new obj"""
        self.__session.add(obj)

    def save(self):
        """commit all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload all tables"""
        Base.metadata.create_all(self.__engine)
        sessionMkr = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(sessionMkr)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.close()
