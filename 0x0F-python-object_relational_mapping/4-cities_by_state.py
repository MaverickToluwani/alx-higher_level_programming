#!/usr/bin/python3
""" A script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY %s", (id, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
