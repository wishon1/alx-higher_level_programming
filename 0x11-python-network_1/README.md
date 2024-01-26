# 0x11. Python - Network #1
![Python](https://img.shields.io/badge/Python-v3.8.5-blue)

## Description
This project builds upon the foundational network programming skills developed in the previous project, focusing on fetching internet resources, decoding responses, and using Python packages like urllib and requests. The tasks cover topics such as HTTP requests, response handling, and interacting with APIs.

## Resources
Read or watch:

- [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/)
- [Requests package](https://pypi.org/project/requests/)

## Project Structure
- `0-hbtn_status.py`: Python script to fetch and display the status of https://alx-intranet.hbtn.io using urllib.
- `1-hbtn_header.py`: Python script to take a URL, send a request, and display the value of the X-Request-Id variable in the header using urllib.
- `2-post_email.py`: Python script to send a POST request with an email parameter to a specified URL using urllib.
- `3-error_code.py`: Python script to handle HTTP errors and display the body of the response using urllib.
- `4-hbtn_status.py`: Python script to fetch and display the status of https://alx-intranet.hbtn.io using requests.
- `5-hbtn_header.py`: Python script to take a URL, send a request, and display the value of the X-Request-Id variable in the response header using requests.
- `6-post_email.py`: Python script to send a POST request with an email parameter to a specified URL using requests.
- `7-error_code.py`: Python script to handle HTTP errors and display the body of the response using requests.
- `8-json_api.py`: Python script to send a POST request with a letter parameter to http://0.0.0.0:5000/search_user and display the result using requests.
- `10-my_github.py`: Python script to authenticate with GitHub API using Basic Authentication and display the user id.

## Prerequisites
- Python 3.8.5 installed.
- Basic Python knowledge.
- Understanding of network concepts (HTTP requests, headers).

## Learning Objectives
After completing this project, i should be able to explain key concepts without Google's help, including fetching internet resources, handling HTTP errors, making POST requests, and interacting with APIs using Python.

## Requirements
- Allowed editors: vi, vim, emacs.
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- A README.md file at the root of the repo, containing a description of the repository.
- Your code should use pycodestyle (version 2.8.*).
- All files must be executable.
- The length of your files will be tested using wc.
- All modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)').
- You must use `get` to access dictionary values by key.
- Documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method.
- Your code should not be executed when imported (by using `if __name__ == "__main__":`).

## Tasks
### 0. What's my status? #0
Write a Python script that fetches https://alx-intranet.hbtn.io/status using the urllib package.

Example:
```bash
$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
```

### 1. Response header value #0
Write a Python script that takes in a URL, sends a request, and displays the value of the X-Request-Id variable found in the header of the response using urllib.

Example:
```bash
$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
```

### 2. POST an email #0
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8) using urllib.

Example:
```bash
$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
```

### 3. Error code #0
Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response (decoded in utf-8) using urllib. Handle urllib.error.HTTPError exceptions.

Example:
```bash
$ ./3-error_code.py http://0.0.0.0:5000
Index
$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
```

### 4. What's my status? #1
Write a Python script that fetches https://alx-intranet.hbtn.io/status using the requests package.

Example:
```bash
$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
```

### 5. Response header value #1
Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the variable X-Request-Id in the response header using requests.

Example:
```bash
$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
```

### 6. POST an email #1
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response using requests.

Example:
```bash
$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
```

### 7. Error code #1
Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response using requests. If the HTTP status code is greater than or equal to 400, print "Error code:" followed by the value of the HTTP status code.

Example:
```bash
$ ./7-error_code.py http://0.0.0.0:5000
Index
$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
$ ./7-error_code.py http://0.0
