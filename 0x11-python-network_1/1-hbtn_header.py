#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable 
found in the header of the response.
"""
import urllib.request
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print(request_id)
        else:
            print("X-Request-Id not found in the response headers.")
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code} - {e.reason}")
except urllib.error.URLError as e:
    print(f"Failed to fetch data. Error: {e}")
