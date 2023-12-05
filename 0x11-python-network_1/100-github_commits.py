#!/usr/bin/python3
"""
Takes 2 arguments and list 10 commits
of the repo name by the user.
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    r = requests.get(url)
    commits = r.json()

    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"),
                commits[i].get("commit")
                .get("author").get("name")))
    except IndexError:
        pass
