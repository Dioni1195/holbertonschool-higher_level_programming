#!/usr/bin/python3
""" This module adds all arguments to a list and save
them to a file
"""
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
args = []
try:
    args = load_from_json_file('add_item.json')
except FileNotFoundError:
    save_to_json_file([], 'add_item.json')
for i in sys.argv[1:]:
    args.append(i)
save_to_json_file(args, 'add_item.json')
