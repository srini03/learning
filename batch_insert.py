import cx_Oracle
import db_config

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)

cursor=con.cursor()
data = [
    (110, "Parent 110"),
    (120, "Parent 120"),
    (130, "Parent 130"),
    (140, "Parent 140"),
    (150, "Parent 150")
]
 
for row in data:
    cursor.execute("""
            insert into ParentTable (ParentId, Description)
            values (:1, :2)""", row)
con.commit()