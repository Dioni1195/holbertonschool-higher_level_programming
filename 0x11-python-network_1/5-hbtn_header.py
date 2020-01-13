#!/usr/bin/python3
""" Find a header variable using requests """
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers['X-Request-Id'])
