#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column("name", String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """list of city"""
            list_fo_city = []
            for n in list(models.storage.all(City).values()):
                if self.id == n.state_id:
                    list_fo_city.append(n)
            return list_fo_city
