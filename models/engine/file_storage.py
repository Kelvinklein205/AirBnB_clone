#!/usr/bin/python3
'''This module contain the `FileStorage` class that
serializes instances to JSON fileand deserializes
JSON file to instances
'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''Manages the database for our objects

    Private class attribute:
        __file_path (str): string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by
            <class name>.id (ex: to store a BaseModel object with
            id=12121212, the key will be BaseModel.12121212)
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in `__objects` the `obj` with <obj class name>.id

        Args:
        obj (obj of a valid class): an object of one of our classes
        '''
        string = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[string] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as fd:
            json.dump(new_dict, fd)

    def reload(self):
        '''deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        '''

        try:
            with open(self.__file_path, 'r') as fd:
                self.__objects = json.load(fd)

            for key, value in self.__objects.items():
                class_name = key.split('.')[0]
                self.__objects[key] = eval(class_name)(**value)

        except FileNotFoundError:
            return
