#!/usr/bin/python3
"""Command interpreter for HBNB project"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    valid_classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]

    def emptyline(self):
        """Do nothing on an empty line (pressing ENTER)"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.valid_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(args[0], instance_id)
                objects = storage.all()
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.valid_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(args[0], instance_id)
                objects = storage.all()
                if key in objects:
                    del objects[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        elif arg not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objects.items() if key.startswith(arg + '.')])
    
    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_id = args[1]
            key = "{}.{}".format(args[0], instance_id)
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attribute_name = args[2]
                attribute_value = args[3]
                instance = objects[key]
                try:
                    # Try to set the attribute dynamically
                    setattr(instance, attribute_name, attribute_value)
                    instance.save()
                except AttributeError:
                    print("** attribute name doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
