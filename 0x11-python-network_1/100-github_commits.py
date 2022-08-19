#!/usr/bin/python3
"""list 10 commits from the repository"""
import requests
import sys


if __name__ == "__main__":
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)
    commits = response.json()
    for commit in commits:
        print(commit)
