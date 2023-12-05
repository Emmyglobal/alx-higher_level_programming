#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the body of the response
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    if hasattr(req, 'status_code') and req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)
