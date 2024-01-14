#!/usr/bin/python3
""" script that takes in an argument and displays all values in
    the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    db_interact = db.cursor()

    # Use format to create the SQL query with the user input
    db_interact.execute("SELECT * FROM `states` WHERE `name` = '{}'\
                         ORDER BY `id`".format(argv[4]))

    for state in db_interact.fetchall():
        if state[1] == argv[4]:
            print(state)

    db_interact.close()
    db.close()
