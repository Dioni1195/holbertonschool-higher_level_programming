#!/usr/bin/python3
""" Display body of the response using requests """
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        let = argv[1]
    else:
        let = ""
    value = {'q': let}
    req = requests.post('http://0.0.0.0:5000/search_user', data=value)
    json = req.json()
    if len(json) == 0:
        print('No result')
    else:
        try:
            print('[{}] {}'.format(json['id'], json['name']))
        except Exception:
            print("Not a valid JSON")
