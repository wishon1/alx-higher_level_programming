#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)

- The email must be sent in the email variable
- use the packages urllib and sys
- You are not allowed to import packages other than urllib and sys
- You don’t need to check arguments passed to the script (number or type)
- You must use the with statement
"""
from sys import argv
from urllib import parse, request


def post_request(url, email):
    """send a post request to the passed url"""
    dict_val = {"email": email}
    # convert the value to urlcode format and then to byte(asccii)
    data = parse.urlencode(dict_val)
    data = data.encode('ascii')

    # send data to url as a request
    content = request.Request(url, data)
    with request.urlopen(content) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    post_request(url, email)
