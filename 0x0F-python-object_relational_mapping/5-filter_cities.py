#!/usr/bin/python3
""" A  script that takes in the name of a state as an
    argument and lists all cities of that state, using
    the database hbtn_0e_4_usa
"""

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
    cur.execute(
            "SELECT cities.name FROM cities INNER JOIN states\
                    ON cities.state_id = states.id\
                    WHERE states.name = %s\
                    ORDER BY cities.id ASC", (argv[4], )
                    )
    rows = cur.fetchall()
    num_cities = len(rows)
    count = 0
    for row in rows:
        for col in row:
            res = f"{col}, " if count < num_cities-1 else col
        print(res, end="")
        count += 1
    print()

    cur.close()
    db.close()
