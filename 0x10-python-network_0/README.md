# 0x10. Python - Network #0
![Python](https://img.shields.io/badge/Python-v3.8.5-blue)

## Description
This project focuses on foundational network programming skills using Python, covering essential concepts like sockets, TCP/IP communication, and client-server architecture.

## Project Structure
- `client.py`: Code for the client-side.
- `server.py`: Code for the server-side.
- `utils.py`: Utility functions for both client and server.
- `README.md`: Project documentation.

## Resources
Resources
Read or watch:

- [HTTP (HyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html) (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)


## Prerequisites
- Python 3 installed.
- Basic Python knowledge.
- Understanding of networking concepts (IP addresses, ports).

## Learning Objectives
After completing this project, you should be able to explain key concepts without Google's help, including HTTP, URL components, HTTP methods, headers, and cookies.

## Requirements
- Bash scripts 3 lines long, ending with a new line, and executable.
- Python scripts using pycodestyle, documented modules, classes, and functions.
- Successful completion of the quiz without plagiarism.

## Tasks
### 0. cURL body size
Write a Bash script that takes a URL, sends a request, and displays the response body size in bytes using `curl`.

Example:
```bash
$ ./0-body_size.sh 0.0.0.0:5000
10
```

### 1. cURL to the end
Write a Bash script that takes a URL, sends a GET request, and displays the body of a 200 status code response.

Example:
```bash
$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
```

### 2. cURL Method
Write a Bash script that sends a DELETE request to a URL and displays the response body.

Example:
```bash
$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
```

### 3. cURL only methods
Write a Bash script that takes a URL and displays all accepted HTTP methods using `curl`.

Example:
```bash
$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
```

### 4. cURL headers
Write a Bash script that sends a GET request to a URL with a specific header and displays the response body.

Example:
```bash
$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!
```

### 5. cURL POST parameters
Write a Bash script that sends a POST request with parameters to a URL and displays the response body.

Example:
```bash
$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
```

### 6. Find a peak
Write a Python function to find a peak in an unsorted list of integers with the lowest complexity.

Example:
```python
$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
```
