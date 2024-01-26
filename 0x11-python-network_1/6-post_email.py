#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST request to
   the passed URL with the email as a parameter, and finally displays the body
   of the response
"""
from sys import argv
import requests


def send_post_request(url, email):
    """sends a POST request to the passed URL with the email as a parameter"""
    email_dict = {"email": email}
    response = requests.post(url, data=email_dict)
    print(response.text)


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    send_post_request(url, email)
