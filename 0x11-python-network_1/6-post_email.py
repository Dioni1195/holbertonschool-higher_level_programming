#!/usr/bin/python3
""" Find a header variable using requests """
import requests
from sys import argv

if __name__ == "__main__":
    value = {'email': argv[2]}
    req = requests.post(argv[1], data=value)
    print(req.text)
