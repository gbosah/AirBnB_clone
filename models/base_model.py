#!/usr/bin/python3
"""Module for base model"""

from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel():
    """This is the base model class for AirBnB project"""
    def __init__(self, *args, **kwargs):
        """Initialize Public Instance"""
        timeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now
        self.updated_at = datetime.now
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created at", "updated at"):
                    value = datetime.strptime(value, timeFormat)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            storage.new(self)

    def save(self):
        """Updates the public class instance updated_at with the current time and date"""
        self.updated_at = datetime.now
        storage.save()

    def to_dict(self):
        """Returns the dictionary of the BaseModel instance"""
        dct = dict(self.__dict__)
        dct["created_at"] = dct["created_at"].isoformat()
        dct["updated_at"] =dct["updated_at"].isoformat()
        dct["__class__"] = self.__self__class__.__name__
        return dct

    def __str__(self):
        """Return the str representation of the BaseModel instance"""
        return "[{}]({}){}".format(self.__class__.__name__,
        self.id, self.__dict__)

