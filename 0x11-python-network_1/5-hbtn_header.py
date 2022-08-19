#!/usr/bin/python3
"""send request and display the value of X-Request-Id"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
