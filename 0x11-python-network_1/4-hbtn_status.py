#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests


def fetch_data(data):
    """scripts that fetches https://alx-intranet.hbtn.io/status"""
    request = requests.get(data)
    print("Body response")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_data(url)
