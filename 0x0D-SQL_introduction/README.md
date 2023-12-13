* Project: 0x0D. SQL - Introduction

* Resources
+ Read or watch:

+ [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
+ [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
+ [Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
+ [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
+ [SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
+ [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
+ [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
+ [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
+ [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
+ [installing MySQL in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)

* Requirements
+ General
+ Allowed editors: vi, vim, emacs
+ All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
+ All your files should end with a new line
+ All your SQL queries should have a comment just before (i.e. syntax above)
+ All your files should start by a comment describing the task
+ All SQL keywords should be in uppercase (SELECT, WHERE…)
+ A README.md file, at the root of the folder of the project, is mandatory
+ The length of your files will be tested using wc

* Tasks:
+ 0. List databases
+ Write a script that lists all databases of your MySQL server.

1. Create a database
+ Write a script that creates the database hbtn_0c_0 in your MySQL server.
+ If the database hbtn_0c_0 already exists, your script should not fail
+ You are not allowed to use the SELECT or SHOW statements
+ File: 1-create_database_if_missing.sql

2. Delete a database
+ Write a script that deletes the database hbtn_0c_0 in your MySQL server.
+ If the database hbtn_0c_0 doesn’t exist, your script should not fail
+ You are not allowed to use the SELECT or SHOW statements

3. List tables
+ Write a script that lists all the tables of a database in your MySQL server.
+ The database name will be passed as argument of mysql command (in the following example: 
  mysql is the name of the database)
+ File: 3-list_tables.sql

4. First table
+ Write a script that creates a table called first_table in the current database in your MySQL server.
+ first_table description:
+ id INT
+ name VARCHAR(256)
+ The database name will be passed as an argument of the mysql command
+ If the table first_table already exists, your script should not fail
+ You are not allowed to use the SELECT or SHOW statements
+ File: 4-first_table.sql

5. Full description.
+ Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
+ The database name will be passed as an argument of the mysql command
+ You are not allowed to use the DESCRIBE or EXPLAIN statements
+ File: 5-full_table.sql

6. List all in table
+ Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
+ All fields should be printed
+ The database name will be passed as an argument of the mysql command
+ File: 6-list_values.sql
 
