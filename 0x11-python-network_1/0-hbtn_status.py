#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        content = response.read()
        content_str = content.decode("utf-8")
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content_str)
except urllib.error.URLError as e:
    print(f"Failed to fetch data. Error: {e}")
