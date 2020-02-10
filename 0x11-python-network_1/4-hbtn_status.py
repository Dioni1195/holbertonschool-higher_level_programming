#!/usr/bin/python3
""" Fletcha url using requests """
import requests

if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(req.text))
    print('\t- content:', req.text)
