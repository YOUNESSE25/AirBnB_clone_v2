#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models




Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column("id", String(60), nullable=False, primary_key=True)
    created_at = Column("created_at", DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column("updated_at", DateTime, nullable=False, default=(datetime.utcnow()))
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        # storage.new(self)
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at": 
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                #     kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                #                                             '%Y-%m-%dT%H:%M:%S.%f')
                # if key == "updated_at": 
                #     kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                #                                             '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        tt = self.__dict__
        tt.pop("_sa_instance_state", None)
        return '[{}] ({}) {}'.format(cls, self.id, tt)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        my_updated_dict = self.__dict__.copy()
        my_updated_dict["__class__"] = str(type(self).__name__)
        my_updated_dict["created_at"] = self.created_at.isoformat()
        my_updated_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_updated_dict.keys():
            del my_updated_dict['_sa_instance_state']
        return my_updated_dict
    
    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)