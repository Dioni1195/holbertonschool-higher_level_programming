#!/bin/bash
#This script request a URL
curl -w '%{size_download}\n' $1 -so NULL
