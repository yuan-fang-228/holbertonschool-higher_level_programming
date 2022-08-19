#!/usr/bin/python3
"""use GITHub API to display id based on given the username and password"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username_psw = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=username_psw)
    print(response.json().get('id'))
