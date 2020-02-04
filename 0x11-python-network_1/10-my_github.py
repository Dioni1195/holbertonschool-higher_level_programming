#!/usr/bin/python3
""" Display body STARWARS APIusing requests """
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(req.json().get('id'))
