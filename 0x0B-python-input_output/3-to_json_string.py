#!/usr/bin/python3
'''returns JSON representation of an object'''
import json


def to_json_string(my_obj):
    '''function to make python obj a json file'''
    return json.dumps(my_obj)
