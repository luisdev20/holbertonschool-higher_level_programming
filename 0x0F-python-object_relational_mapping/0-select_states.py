#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    con.close()
