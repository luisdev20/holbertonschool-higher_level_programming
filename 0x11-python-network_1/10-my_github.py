#!/usr/bin/python3
"""Takes Github credentials and uses Github API to display your ID
"""
import requests
import sys

if __name__ == "__main__":
user = sys.argv[1]
password = sys.argv[2]
url = "https://api.github.com/user"

req = requests.get(url, auth=(user, password))
req_json_rep = req.json()

print(req_json_rep.get("id", "None"))
