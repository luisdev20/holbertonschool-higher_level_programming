#!/bin/bash
# Get the body's bit size of the response header
curl -s "$1" | wc -c
