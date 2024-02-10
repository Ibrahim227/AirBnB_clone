#!/usr/bin/python3
"""import erequired module"""
from base_model import BaseModel


class User(BaseModel):
    """class that inherit from baseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""        
