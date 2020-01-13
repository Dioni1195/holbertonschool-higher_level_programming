#!/usr/bin/python3
""" Display body of the response using requests """
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    status = req.status_code
    if status >= 400:
        print('Error code: ', status)
    else:
        print(req.text)
