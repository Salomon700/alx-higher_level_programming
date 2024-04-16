#!/usr/bin/python3
"""define a string to json function"""
import json


def to_json_string(my_obj):
    """function that returns the JSON of a string"""
    return json.dumps(my_obj)
