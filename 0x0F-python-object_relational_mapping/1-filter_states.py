#!/usr/bin/python3

"""A script that list all states with a
name starting with 'N' from hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY \
                    'N%' ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
