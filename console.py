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
from models import storage


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
        le = split(arg[:cbr.span()[0]])
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
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
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
        arg0 = parse(arg)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg0[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg0[0])().id)
            storage.save

    def do_show(self, arg):
        """Prints the str representation of an instance"""
        arg0 = parse(arg)
        disp_dict = storage.all()
        if len(arg0) == 0:
            print("** class name missing **")
        elif arg0[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg0) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg0[0], arg0[1]) not in disp_dict:
            print("** no instance found **")
        else:
            print(disp_dict["{}.{}".format(arg0[0], arg0[1])])

    def do_destroy(self, arg):
        """Deletes an instance and save the change to JSON file"""
        arg0 = parse(arg)
        del_dict = storage.all()
        if len(arg0) == 0:
            print("** class name missing **")
        elif arg0[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg0) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg0[0], arg0[1]) not in del_dict.keys():
            print("** no instance found **")
        else:
            del del_dict["{}.{}".format(arg0[0], arg0[1])]
            storage.save()

    def do_all(self, arg):
        """Prints str representations of all instances"""
        arg0 = parse(arg)
        if len(arg0) > 0 and arg0[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(arg0) > 0 and arg0[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(arg0) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """retrieve the num of instances of a given class"""
        arg0 = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg0[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Updates and instance by add/update attr, save change to JSON file"""
        arg0 = parse(arg)
        updobjdict = storage.all()

        if len(arg0) == 0:
            print("** class name missing **")
            return False
        if arg0[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg0) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg0[0], arg0[1]) not in updobjdict.keys():
            print("** no instance found **")
            return False
        if len(arg0) == 2:
            print("** attribute name missing **")
            return False
        if len(arg0) == 3:
            try:
                type(eval(arg0[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg0) == 4:
            obj = updobjdict["{}.{}".format(arg0[0], arg0[1])]
            if arg0[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg0[2]])
                obj.__dict__[arg0[2]] = valtype(arg0[3])
            else:
                obj.__dict__[arg0[2]] = arg0[3]
        elif type(eval(arg0[2])) == dict:
            obj = updobjdict["{}.{}".format(arg0[0], arg0[1])]
            for k, v in eval(arg0[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
