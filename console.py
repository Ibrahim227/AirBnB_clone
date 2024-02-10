#!/usr/bin/python3
"""Import required modules"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the CLi"""
    prompt = '(hbnb)'

    def do_help(self, arg):
        """Handle help command"""
        pass

    def do_quit(self):
        """quit command to exit the program"""
        pass

    def do_EOF(self):
        """Handle end of file"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
