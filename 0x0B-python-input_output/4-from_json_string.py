#!/usr/bin/python3
"""A module that returns an object(Python data structure) by JSON"""
import json


def from_json_string(my_str):
    """returns an object"""
    return json.loads(my_str)
