#!/usr/bin/python3
"""a script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa where name m
atches the argument that is safe from MySQL injections
"""

import MySQLdb
from sys import argv

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (argv[4], ))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
