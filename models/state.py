#!/usr/bin/python3
""""import the required module"""
from models.base_model import BaseModel


class State(BaseModel):
    """class that inherit fromBaseMOdel"""
    name: str = ""
