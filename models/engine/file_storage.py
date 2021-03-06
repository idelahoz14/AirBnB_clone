#!/usr/bin/python3
"""FileStorage module
"""
import json


class FileStorage():
    """
    BaseModel constructor.
    """
    def __init__(self):
        """serializes instances to a JSON file and deserializes
        JSON file to instances

        Args: Private class attributes.
            file_path (string): string - path to the JSON file.
            objects (dictionary): mpty but will store all objects
            by <class name>.id
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Public methot that returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id.

        Args:
            obj ([type]): object to set in __objects.
        """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path).
        """
        filepath = self.__file_path
        listDict = {}
        if self.__objects is not None:
            for key, value in self.__objects.items():
                dictionary = value.to_dict()
                listDict[key] = dictionary
        jstring = json.dumps(listDict)
        with open(filepath, 'w') as f:
            f.write(jstring)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as f:
                diccionario = json.load(f)
            from models.base_model import BaseModel
            for key, value in diccionario.items():
                self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
