#!/usr/bin/python3
"""fetch URL and display as required"""
import requests


if __name__ == "__main__":
    r = request.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
