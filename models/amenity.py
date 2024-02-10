#!/usr/bin/python3
"""import required module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class that inherit from BaseModel"""
    name: str = ""
