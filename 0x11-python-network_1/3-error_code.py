#!/usr/bin/python3
"""Sends a request to the URL and displays the response body in utf-8.

Usage: ./3-error_code.py
- Handles and print HTTPError
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
