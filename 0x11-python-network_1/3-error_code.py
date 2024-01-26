#!/usr/bin/python3
"""script takes in a URL, sends a request to the URL and displays the body of
   the response (decoded in utf-8).
"""
from urllib import request, error
from sys import argv


def sendRequest_to_url(http_url):
    """send request to the http_url"""
    try:
        with request.urlopen(http_url) as response:
            content = response.read().decode('UTF-8')
            print(content)
    except error.HTTPError as e:
        print('Error code:', e.code)


if __name__ == "__main__":
    url = argv[1]
    sendRequest_to_url(url)
