#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
   the body of the response.
"""
from sys import argv
import requests


def sendRquestTo_url_displayTheBody(url_code):
    """equest to the URL and displays the body of the response."""
    response = requests.get(url_code)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    url = argv[1]
    sendRquestTo_url_displayTheBody(url)
