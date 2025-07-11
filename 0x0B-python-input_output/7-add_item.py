#!/usr/bin/python3
"""Adds all arguments to a python list, and then save them to a file"""
import sys
save2json = __import__("5-save_to_json_file").save_to_json_file
load4rm = __import__("6-load_from_json_file").load_from_json_file

try:
    my_list = load4rm("add_item.json")
except FileNotFoundError:
    my_list = []

my_list.extend(sys.argv[1:])
save2json(my_list, "add_item.json")
