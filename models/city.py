#!/usr/bin/python3
"""import the required module"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherit from BaseModel"""
    state_id: str = ""
    name: str = ""
