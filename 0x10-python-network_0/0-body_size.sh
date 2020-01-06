#!/bin/bash
#This script request a URL
curl -w %{size_download} $1 -so NULL
echo
