#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


def postRequest_with_letter(parameter):
    """Takes in a letter and sends a POST request."""
    url = "http://0.0.0.0:5000/search_user"

    # Letter must be sent in variable q
    val = {'q': parameter}

    # Send POST request to the specified URL with the letter as a parameter
    response = requests.post(url, data=val)

    try:
        # Attempt to parse the response body as JSON
        parsed_response = response.json()

        if not parsed_response:
            # If JSON is empty, display 'No result'
            print("No result")
        else:
            # If JSON is not empty, display the id and name
            print("[{}] {}".format(parsed_response.get(
                "id"), parsed_response.get("name")))
    except ValueError:
        # If the JSON is not properly formatted, display 'Not a valid JSON'
        print("Not a valid JSON")


if __name__ == "__main__":
    # Check if an argument is provided, if not, set q=""
    if len(argv) == 1:
        param = ""
    else:
        param = argv[1]

    postRequest_with_letter(param)
