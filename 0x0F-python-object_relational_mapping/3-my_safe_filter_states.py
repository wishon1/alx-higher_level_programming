#!/usr/bin/python3

'''This script takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where the name matches the argument. It is designed to be
safe from MySQL injections.

Usage:
    ./safe_filter_states.py [mysql_username] [mysql_password] [database_name]
    [state_name]

Arguments:
    mysql_username: The MySQL username for database connection.
    mysql_password: The MySQL password for database connection.
    database_name: The name of the MySQL database.
    state_name: The name of the state to search for in the states table.

Example:
    ./safe_filter_states.py root password hbtn_0e_0_usa "Arizona"

Note:
    This script connects to a MySQL server running on localhost at port 3306.
    Results are sorted in ascending order by states.id and displayed as per the
    example below.'''
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host="localhost", port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM `states` WHERE `name` = %s ORDER BY `id`",
              (argv[4],))

    for state in c.fetchall():
        print(state)

    c.close()
    db.close()
