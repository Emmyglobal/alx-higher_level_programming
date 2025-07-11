#!/usr/bin/python3
"""A function that converts object to dictionary for easy dumping"""


def class_to_json(obj):
    """Returns dictionary"""
    return obj.__dict__
