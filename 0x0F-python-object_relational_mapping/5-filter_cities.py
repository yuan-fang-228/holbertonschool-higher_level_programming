#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name \
                FROM cities INNER JOIN states \
                ON cities.state_id=states.id and states.name=%s",
                {sys.argv[4]})
    rows = cur.fetchall()
    result = []
    for row in rows:
        result.append(row[0])
    print(', '.join(result))
    cur.close()
    db.close()
