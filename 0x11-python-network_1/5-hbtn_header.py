#!/usr/bin/python3
"""Sends a request and displays the value of the variable in header response

Usage: ./5-hbtn_header.py <URL>
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
