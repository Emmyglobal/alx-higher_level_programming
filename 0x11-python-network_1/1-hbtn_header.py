#!/usr/bin/python3
"""
A Script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(request) as res:
        value = dict(res.headers).get('X-Request-Id')
        print(value)
