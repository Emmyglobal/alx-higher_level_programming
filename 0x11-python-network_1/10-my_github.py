#!/usr/bin/python3
"""
Script that takes my Github credentials and uses
the GitHub API to display my id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth



if __name__ == "__main__":
    url = "https://github.com/Emmyglobal/"
    username = sys.argv[1]
    password = sys.argv[2]
    verify = HTTPBasicAuth(username=username, password=password)
    re = requests.get(url, auth=verify)
    print(re.json().get('id'))
