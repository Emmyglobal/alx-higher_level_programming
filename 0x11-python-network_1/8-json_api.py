#!/usr/bin/python3
"""
Script that takes in a letter and sends a post request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        value = ""
    else:
        value = sys.argv[1]
    try:
        val = {'q': value}
        req = requests.post(url, data=val)
        if req.json() == {}:
            print("No result")
        else:
            print(f"[{(req.json()).get('id')}]) {(req.json()).get('name')}")
    except ValueError:
        print("Not a valid JSON")
