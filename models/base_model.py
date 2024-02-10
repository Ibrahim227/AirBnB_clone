#!/usr/bin/python3
"""Import required module"""
import models
from datetime import datetime
import uuid


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
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """update datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """return a dictionnary of keys/values"""
        rtdict = self.__dict__.copy()
        rtdict["created_at"] = self.created_at.isoformat()
        rtdict["updated_at"] = self.updated_at.isoformat()
        rtdict["__class__"] = self.__class__.__name__
        return rtdict

    def __str__(self):
        ClassName = self.__class__.__name__
        return "[{}] ({}) {}".format(ClassName, self.id, self.__dict__)
