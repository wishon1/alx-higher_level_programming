#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the
   value of the variable X-Request-Id in the response header
"""
import requests
from sys import argv


def send_request_to_url_display_requestId(url):
    """send request to url and display value of request id"""
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    url = argv[1]
    send_request_to_url_display_requestId(url)
