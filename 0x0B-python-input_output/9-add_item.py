#!/usr/bin/python3
""" This module adds all arguments to a list and save
them to a file
"""
import sys


save_to_json_file = __import__('7-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file.py').load_from_json_file
print(sys.argv)