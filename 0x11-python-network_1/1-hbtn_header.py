#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable 
found in the header of the response.
"""

import sys
import urllib.request

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print("X-Request-Id:", request_id)
        else:
            print("X-Request-Id not found in the response headers.")
except urllib.error.URLError as e:
    print(f"Failed to fetch data. Error: {e}")
