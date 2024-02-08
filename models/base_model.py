#!/usr/bin/python3
"""Import required module"""
from datetime import datetime
import uuid


class BaseModel:
    """Class for all other classes to inherit from"""
    def __init__(self):
        """method to instantiate an instance of BaseMOdel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """update datetime"""
        return updated_at
