#!/bin/bash
#This script request a URL
curl -si $1 -X OPTIONS | grep 'Allow:' | cut -d ' ' -f2-
