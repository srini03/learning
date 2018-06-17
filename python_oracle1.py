from __future__ import print_function

import cx_Oracle
import db_config

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
cur = con.cursor()

#cur.executemany("insert into mytab(id, data) values (:1, :2)", rows)

# Now query the results back

cur2 = con.cursor()
cur2.execute('select * from ChildTable')
res = cur2.fetchall()
print(res)
