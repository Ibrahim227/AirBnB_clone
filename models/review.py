#!/usr/bin/python3
"""import required modue"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review inherit from BaseModel"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
