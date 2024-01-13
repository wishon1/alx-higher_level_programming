#!/usr/bin/python3
"""
    lists all states with a name starting with N (upper N) from the
    database hbtn_0e_0_usa:
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    interact_db = db.cursor()
    interact_db.execute("SELECT * FROM 'states' ORDER BY 'id'")

    for state in interact_db.fetchall():
        if state[1][0] == 'N':
            print(state)

    db.close()
