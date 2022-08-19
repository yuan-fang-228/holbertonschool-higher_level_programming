#!/usr/bin/python3
"""display the value of X-Request-Id found in header"""
import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.headers['X-Request-Id'])
