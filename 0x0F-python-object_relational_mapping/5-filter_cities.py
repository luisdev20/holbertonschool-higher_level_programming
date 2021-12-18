#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                 INNER JOIN `states` as `s` \
                 ON `c`.`state_id` = `s`.`id` \
                 ORDER BY `c`.`id`")
    query_rows = cur.fetchall()
    x = []
    for row in query_rows:
        if row[2] == sys.argv[4]:
            x.append(row[1])
    print(", ".join(x))
    cur.close()
    db.close()
