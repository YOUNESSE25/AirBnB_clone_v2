#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
import models
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column("city_id", String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column("user_id", String(60), ForeignKey("users.id"), nullable=False)
    name = Column("name", String(128), nullable=False)
    description = Column("description", String(1024), nullable=True)
    number_rooms = Column("number_rooms", Integer, default=0, nullable=True)
    number_bathrooms = Column("number_bathrooms", Integer, default=0, nullable=True)
    max_guest = Column("max_guest", Integer, default=0, nullable=True)
    price_by_night = Column("price_by_night", Integer, default=0, nullable=True)
    latitude = Column("latitude", Float, nullable=True)
    longitude = Column("longitude", Float, nullable=True)
    amenity_ids = []
