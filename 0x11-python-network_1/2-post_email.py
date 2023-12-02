#!/usr/bin/python3
"""
Script that takes in a URL and an email,
Send a post request to the passed URL
with the email as a parameter and displays
the body of the response
"""

import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

# Encode the emai; parameter
data = urllib.parse.urlencode({'email': email}).encode('utf-8')
try:
    with urllib.request.urlopen(url, data=data) as response:
        decoded_response = response.read().decode('utf-8')
        print(decoded_response)
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code} - {e.reason}")
except urllib.error.URLError as e:
    print(f"Failed to fetch data. Error: {e}")
