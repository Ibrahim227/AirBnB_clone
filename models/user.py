#!/usr/bin/python3
"""import erequired module"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User inherit from baseModel"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
