#!/usr/bin/python3
""" Display body STARWARS APIusing requests """
import requests
from sys import argv

if __name__ == "__main__":
    value = {'search': argv[1]}
    req = requests.get('https://swapi.co/api/people/', params=value)
    response = req.json()
    print("Number of results: {}".format(response.get('count')))
    list_rest = response.get('results')
    for res in list_rest:
        print(res.get('name'))
