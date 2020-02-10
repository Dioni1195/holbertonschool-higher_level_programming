#!/usr/bin/python3
""" displays the value of the X-Request-Id variable found in the header """
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    email = {'email': argv[2]}
    url = argv[1]
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
