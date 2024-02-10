#!/usr/bin/python3
"""import required modue"""
from base_model import BaseModel


class Review(BaseModel):
    """class that inherit from BaseModel"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
    super().__init__(self)
