#!/usr/bin/python3
"""Import required modules"""
import cmd
import sys
import models
from models.review import Review
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.engine.file_storage import FileStorage



class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the CLi"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """quit command to exit the program"""
        sys.exit()

    def do_EOF(self, arg):
        """End of file"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON"""
        pass

    def do_show(self, arg):
        """Prints the str representation of an instance"""
        pass

    def do_destroy(self, arg):
        """Deletes an instance and save the change to JSON file"""
        pass

    def do_all(self, arg):
        """Prints all str representations of all instances"""
        pass

    def do_update(self, arg):
        """Updates and instance by add/update attr, save change to JSON file"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
