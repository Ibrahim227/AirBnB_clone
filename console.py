#!/usr/bin/python3
"""Import required modules"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the CLi"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """quit command to exit the program"""
        sys.exit()

    def do_EOF(self, arg):
        """End of file"""
        pass

    def create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON"""
        pass

    def show(self, arg):
        """Prints the str representation of an instance"""
        pass

    def destroy(self, arg):
        """Deletes an instance and save the change to JSON file"""
        pass

    def all(self, arg):
        """Prints all str representations of all instances"""
        pass

    def update(self, arg):
        """Updates and instance by add/update attr, save change to JSON file"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
