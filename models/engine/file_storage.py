#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
from models.base_model import BaseModel

class FileStorage:
     """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)
    
    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                'BaseModel': BaseModel,
                'User': User,
                'Place': Place,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Review': Review
                }
        try:
            data = {}
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    if class_name in classes:
                        self.all()[key] = classes[class_name](**value)
        except FileNotFoundError:
            pass
