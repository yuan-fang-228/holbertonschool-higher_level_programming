#!/usr/bin/python3
"""send POST request with letter as parameter"""
import requests
import sys


if __name__ == "__main__":
    letter = ""
    if len(sys.argv) == 1:
        letter = sys.argv[1]
    value = {'q': letter}
    p = requests.post('http://0.0.0.0:5000/search_user', data=value)
    try:
        if p.json():
            print('[{}] {}'.format(p.json().get('id'), p.json().get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
