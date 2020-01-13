#!/usr/bin/python3
""" displays the value of the X-Request-Id variable found in the header """
import urllib.parse
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.URLError as er:
            print('Error code:', er.code)
