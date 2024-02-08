#!/usr/bin/python3
"""Import required module"""
from datetime import datetime
import uuid


class BaseModel:
    """Class for all other classes to inherit from"""
    def __init__(self):
        """method to instantiate an instance of BaseMOdel"""
        self.id = str(uuid.uuid4())
