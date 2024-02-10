#!/usr/bin/python3
"""Import required modules"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the CLi"""
    def __init__(self):
        """instantiate the class definition"""
        pass

    def do_help(self):
        """Handle help command"""
        pass

    def do_quit(self):
        """handle the quit command"""
        pass

    def do_EOF(self):
        """Handle end of file"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
