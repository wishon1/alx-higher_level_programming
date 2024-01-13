# Project Title: Python - Object-relational mapping

## Description
This project focuses on connecting Python with databases using the Object-Relational Mapping (ORM) approach. It involves using both the `MySQLdb` module and `SQLAlchemy`, an ORM. The primary goal is to interact with a MySQL database, execute SQL queries, and then transition to using an ORM to abstract away the storage details.

## Background Context
In the first part, the project uses the `MySQLdb` module to connect to a MySQL database and execute SQL queries. The second part introduces the use of `SQLAlchemy`, an Object-Relational Mapper (ORM), eliminating the need for direct SQL queries in Python code.

## Key Concepts
- Python programming and its advantages
- Connecting to a MySQL database using Python
- Executing SELECT and INSERT queries in MySQL from Python
- Introduction to Object-Relational Mapping (ORM) with SQLAlchemy
- Mapping a Python class to a MySQL table
- Creating a Python Virtual Environment

## Resources
- Read or watch:

- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [mysqlclient/MySQLdb documentation (please don’t pay attention to \_mysql)](https://mysqlclient.readthedocs.io/)
- [MSQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
- [mysqlclient/MySQLdb](https://www.youtube.com/watch?v=woKYyhLCcnU)
- [Introduction to SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
- [Flask SQLAlchemy](https://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
- [10 common stumbling blocks for SQLAlchemy newbies](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
- [SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)
- [Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)

## Learning Objectives
Upon completion of this project, you should be able to:
- Explain the benefits of Python programming
- Connect to a MySQL database and execute queries in Python
- Understand the concept of Object-Relational Mapping (ORM)
- Map a Python class to a MySQL table using SQLAlchemy
- Create a Python Virtual Environment

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- Use MySQLdb version 2.0.x and SQLAlchemy version 1.4.x
- Follow specific file structure, naming, and documentation guidelines

## Tasks
### 0. Get all states
- Write a script that lists all states from the database `hbtn_0e_0_usa`.
- Your script should take 3 arguments: MySQL username, MySQL password, and database name.
- Use the module MySQLdb.
- Results must be sorted in ascending order by states.id.

### 1. Filter states
- Write a script that lists all states with a name starting with 'N' (upper N) from the database `hbtn_0e_0_usa`.
- Your script should take 3 arguments: MySQL username, MySQL password, and database name.
- Use the module MySQLdb.
- Results must be sorted in ascending order by states.id.

### 2. Filter states by user input
- Write a script that takes an argument and displays all values in the states table where the name matches the argument.
- Your script should take 4 arguments: MySQL username, MySQL password, database name, and state name searched.
- Use the module MySQLdb.
- Results must be sorted in ascending order by states.id.

### 3. SQL Injection...
- Write a script that displays all values in the states table where the name matches the argument.
- Ensure your script is safe from SQL injection.
- Your script should take 4 arguments: MySQL username, MySQL password, database name, and state name searched.
- Use the module MySQLdb.
- Results must be sorted in ascending order by states.id.

### 4. Cities by states
- Write a script that lists all cities from the database `hbtn_0e_4_usa`.
- Your script should take 3 arguments: MySQL username, MySQL password, and database name.
- Use the module MySQLdb.
- Results must be sorted in ascending order by cities.id.

### 5. All cities by state
- Write a script that lists all cities of a given state from the database `hbtn_0e_4_usa`.
- Your script should take 4 arguments: MySQL username, MySQL password, database name, and state name.
- Use the module MySQLdb.
- Results must be sorted in ascending order by cities.id.

### 6. First state model
- Write a Python file containing the class definition of a State and an instance Base = declarative_base().

### 7. All states via SQLAlchemy
- Write a script that lists all State objects from the database `hbtn_0e_6_usa`.
- Your script should take 3 arguments: MySQL username, MySQL password, and database name.
- Use the module SQLAlchemy.
- Results must be sorted in ascending order by states.id.

### 8. First state
- Write a script that prints the first State object from the database `hbtn_0e_6_usa`.
- Your script should take 3 arguments: MySQL username, MySQL password, and database name.
- Use the module SQLAlchemy.

### 9. Contains `a`
- Write a script that lists all State objects that contain the letter a from the database `hbtn_0e_6_usa`.
- Your script should take 3 arguments: MySQL username, MySQL password, and database name.
- Use the module SQLAlchemy.
- Results must be sorted in ascending order by states.id.

### 10
