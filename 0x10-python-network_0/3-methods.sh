#!/bin/bash
# Get a URL and display all HTTP methods allowed
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
