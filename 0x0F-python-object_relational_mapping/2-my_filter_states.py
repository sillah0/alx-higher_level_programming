#!/usr/bin/python3

"""A script that takes in an argument and displays
all values that matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3])

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
