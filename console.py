#!/usr/bin/python3
"""Import required modules"""
import cmd
import re
from shlex import split
from models.review import Review
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the CLi"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON, prints id"""

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
