#!/usr/bin/python3
"""Import required modules"""
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the CLi"""
    prompt = '(hbnb)'

    def do_help(self, arg):
        """Handle help command"""
        pass

    def do_quit(self, arg):
        """quit command to exit the program"""
        sys.exit()

    def do_EOF(self, arg):
        """Handle end of file"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
