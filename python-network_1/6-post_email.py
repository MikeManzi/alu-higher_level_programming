#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, 
sends a POST request to the passed URL with the email as a parameter, 
and finally displays the body of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    Takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8) using requests
    """
    url = argv[1]
    r = requests.post(url, data={'email': argv[2]})
    print(r.text)