#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.

- You must use the packages urllib and sys
- You are not allow to import packages other than urllib and sys
- The value of this variable is different for each request
- You don’t need to check arguments pa
"""
from sys import argv
from urllib import request


def send_url(url):
    """ send a request to the url and display the value"""
    content = request.Request(url)
    with request.urlopen(content) as response:
        print(dict(response.headers).get("X-Request-Id"))


if __name__ == "__main__":
    url = argv[1]
    send_url(url)
