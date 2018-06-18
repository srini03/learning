import cx_Oracle
import db_config

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)

cursor=con.cursor()
data = [
    (160, "Parent 110"),
    (170, "Parent 120"),
    (180, "Parent 130"),
    (190, "Parent 140"),
    (200, "Parent 150")
]
 
cursor.executemany("""
            insert into ParentTable (ParentId, Description)
            values (:1, :2)""", data)
con.commit()