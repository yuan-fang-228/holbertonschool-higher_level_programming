#!/usr/bin/python3
"""7-add_item Module"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    content = load_from_json_file("add_item.json")
except FileNotFoundError:
    content = []
save_to_json_file(content + sys.argv[1:], "add_item.json")
