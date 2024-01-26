#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    # send a request to  the url and save the content
    with request.urlopen(url) as response:
        content = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- -tf8 content: {}".format(content.decode('utf-8')))
