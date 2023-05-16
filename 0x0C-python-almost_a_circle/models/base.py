#!/usr/bin/python3
'''Defines the base for coming projects'''
import json


class Base:
    '''initializes id'''
    __nb_objects = 0

    def __init__(self, id=None):
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns JSON rep of list of dictionaries'''
        if list_dictionaries == None:
            return ([])
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        '''Returns object rep of JSON string'''
        if json_string == None:
            return []
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        '''saves json list of dictionaries to file'''
        if list_objs is not None:
            list_objs = [o.to_dictionary for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''
            Returns an instance with all the attributes already set
        '''
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r2 = Rectangle(3, 8)
        elif cls.__name__ == "Square":
            r2 = Square(5)
        r2.update(**dictionary)
        return (r2)

    @classmethod
    def load_from_file(cls):
        '''return list of instances from file'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return ([cls.create(**d) for d in cls.from_json_string(f.read())])
