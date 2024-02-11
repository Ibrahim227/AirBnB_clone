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
    cbr = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if cbr is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            le = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in le]
            retl.append(brackets.group())
            return retl
    else:
        le = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in le]
        retl.append(cbr.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the CLi"""
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "City",
        "Place",
        "Review",
        "State",
        "Amenity"
    }

    def emptyline(self):
        """Do nothing until receive a Command"""
        pass

    def default(self, arg):
        """Defaul behavior for The Cmd"""
        default_dict = {
            "all": self.do_all,
            "show": self.so_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in default_dict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return default_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

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
