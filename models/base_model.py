#!/usr/bin/python3
"""Import required module"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Class for all other classes to inherit from"""
    def __init__(self, *ags, **kwargs):
        """method to instantiate an instance of BaseMOdel"""
        dtnow = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or k == "updated_at":
                    self.__dict__[key] = datetime.sstrptime(value, dtnow)
                else:
                    self.__dictpvalue[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """update datetime"""
        return self.updated_at

    def to_dict(self):
        """return a dictionnary of keys/values"""
        return self.__dict__
