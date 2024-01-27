# ALX Higher Level Programming - Python Exceptions

## Overview
This repository contains solutions to various tasks related to handling exceptions in Python. The project covers topics such as safe printing of lists and integers, division operations, and raising exceptions.

## Resources
- **Read or Watch:**
  - [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
  - [Learn to Program 11 Static & Exception Handling (starting at minute 7)](https://www.youtube.com/watch?v=H9Q31N_DrKs)

## Learning Objectives
The learning objectives of this project include understanding the fundamentals of error handling in Python, distinguishing between errors and exceptions, mastering the usage of try-except blocks, knowing when and how to raise exceptions, implementing clean-up actions after exceptions, and preventing plagiarism through independent problem-solving.

## Requirements
The project requires the use of editors like vi, vim, or emacs, all files to be interpreted or compiled on Ubuntu 20.04 LTS with Python version 3.8.5, ensuring that each file concludes with a new line, begins with `#!/usr/bin/python3`, includes a mandatory README.md file at the root of the project folder, follows the PEP 8 style guidelines using pycodestyle (version 2.8.*), and ensures that all files are executable.

## Tasks
### 0. Safe list printing
- Write a function that prints x elements of a list.
  - Prototype: `def safe_print_list(my_list=[], x=0):`
  - Restrictions: Use try-except, no import, no len()

### 1. Safe printing of an integers list
- Write a function that prints an integer with "{:d}".format().
  - Prototype: `def safe_print_integer(value):`
  - Restrictions: Use try-except, "{:d}".format(), no import, no type()

### 2. Print and count integers
- Write a function that prints the first x elements of a list containing only integers.
  - Prototype: `def safe_print_list_integers(my_list=[], x=0):`
  - Restrictions: Use try-except, "{:d}".format(), no import, no len()

### 3. Integers division with debug
- Write a function that divides 2 integers and prints the result.
  - Prototype: `def safe_print_division(a, b):`
  - Restrictions: Use try-except-finally, "{}".format(), no import

### 4. Divide a list
- Write a function that divides element by element 2 lists.
  - Prototype: `def list_division(my_list_1, my_list_2, list_length):`
  - Restrictions: Use try-except-finally, no import

### 5. Raise exception
- Write a function that raises a type exception.
  - Prototype: `def raise_exception():`
  - Restrictions: No import

### 6. Raise a message
- Write a function that raises a name exception with a message.
  - Prototype: `def raise_exception_msg(message=""):`
  - Restrictions: No import
