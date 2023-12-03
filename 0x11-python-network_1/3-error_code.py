#!/usr/bin/python3
"""
Script that takes in a URL
Sends request to the URL and
Displays the body of the response(decode in utf-8)'
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            decoded_response = response.read().decode('utf-8')
            print(decoded_response)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    except urllib.error.URLError as e:
        print(f"Failed to fetch data. Error: {e}")
