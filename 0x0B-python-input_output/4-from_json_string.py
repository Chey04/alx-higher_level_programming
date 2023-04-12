#!/usr/bin/python3
'''returns an object represented by a JSON string'''
import json


def from_json_string(my_str):
    '''function to return python object from JSON representation'''
    return json.loads(my_str)

