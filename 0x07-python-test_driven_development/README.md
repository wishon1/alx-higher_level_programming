Project: 0x07. Python - Test-driven development
concept:
* [Never Forget to Test](https://docs.google.com/document/d/11aTCweT1O8unktCzBDtTOfKDuKUccYSz0XF_jFC1NTs/edit)

* Resources
 - Read or watch:

1. [doctest — Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html)(until “26.2.3.7. Warnings” included)
2. [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
3. [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)
4. [Unittest module](https://www.youtube.com/watch?v=6tNS--WetLI)
5. [Interactive and Non-interactive tests](https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/)

* Tasks:
0. Integers addition
-  Write a function that adds 2 integers.
- Prototype: def add_integer(a, b=98):
-  and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
- a and b must be first casted to integers if they are float
- Returns an integer: the addition of a and b
- You are not allowed to import any module
- File: 2-matrix_divided.py, tests/2-matrix_divided.txt

2. Say my name
- Write a function that prints My name is <first name> <last name>
- Prototype: def say_my_name(first_name, last_name=""):
- first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
- You are not allowed to import any module
- File: 3-say_my_name.py, tests/3-say_my_name.txt

3. Print square
- Write a function that prints a square with the character #.
- Prototype: def print_square(size):
- size is the size length of the square
- size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
- if size is less than 0, raise a ValueError exception with the message size must be >= 0
- if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
- You are not allowed to import any module
- File: 4-print_square.py, tests/4-print_square.txt

4. Text indentation
- Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
- Prototype: def text_indentation(text):
- text must be a string, otherwise raise a TypeError exception with the message text must be a string
- There should be no space at the beginning or at the end of each printed line
- You are not allowed to import any module
- File: 5-text_indentation.py, tests/5-text_indentation.txt

5. Max integer - Unittest
- Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.
- In this task, you will write unittests for the function def max_integer(list=[]):.
- Your test file should be inside a folder tests
- You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- Your test file should be python files (extension: .py)
- Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
- All tests you make must be passable by the function below
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case
