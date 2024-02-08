#!/usr/bin/python3
"""Import required module"""
from datetime import datetime
import uuid


class BaseModel:
    """Class for all other classes to inherit from"""
    def __init__(self):
        """method to instantiate an instance of BaseMOdel"""
        self.id = str(uuid.uuid4())
        self.created_at = isoformat(datetime.now())
        self.updated_at = isoformat(datetime.now())

    def save(self):
        """update datetime"""
        return self.updated_at

    def to_dict(self):
        """return a dictionnary of keys/values"""
        return BaseModel.__dict__
