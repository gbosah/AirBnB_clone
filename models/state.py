#!/usr/bin/python3
"""
Module for State class
"""
from models.base_model import BaseModel
from datetime import datetime
class State(BaseModel):
    """defines State class"""
    name = ""
    def __init__(self, *args, **kwargs):
        """initializes instances"""
        if len(kwargs) > 0:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     self.timeformat)
            if "updated_at" in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                         self.timeformat)
            self.__dict__ = kwargs
        else:
            super().__init__()
