#!/usr/bin/python3
"""use requests to send request and handle error"""
import sys
import requests


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code < 400:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
