#!/usr/bin/python3
"""Import the required module"""
from models.base_model import BaseModel
from models.city import City
from models.state  import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage:
    """Class to serialize/deserialize JSON file"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """instantiate the constructor"""
        pass

    def all(self):
        """returns the dictionnary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in objects the obj"""
        rtname = obj.__class__.__name__
        return rtname

    def save(self):
        """serializes obj to JSON file """
        rtdict = FileStorage.__objects
        objdict = {obj: rtdict[obj].to_dict() for obj in rtdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to obj (only if __file_path exist)"""
        
