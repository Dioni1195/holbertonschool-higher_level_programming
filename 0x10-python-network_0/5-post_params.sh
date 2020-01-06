#!/bin/bash
#This script request a URL
curl -Ls $1 -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
