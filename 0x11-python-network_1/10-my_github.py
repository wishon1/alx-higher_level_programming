#!/usr/bin/python3
"""Script that takes your GitHub credentials (username and password)
   and uses the GitHub API to display your id
"""
from requests.auth import HTTPBasicAuth
from sys import argv
import requests


def displayGitHubId(userName, passWord):
    """Display GitHub id."""
    # GitHub API URL
    url = 'https://api.github.com/user'

    # Use Basic Authentication with a personal access token as the password
    basic_auth = HTTPBasicAuth(userName, passWord)

    # GET request to the GitHub API
    response = requests.get(url, auth=basic_auth)

    print(response.json().get("id"))


if __name__ == "__main__":
    user = argv[1]
    passWord = argv[2]

    displayGitHubId(user, passWord)
