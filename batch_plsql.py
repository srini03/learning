import cx_Oracle
import db_config

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)

cursor=con.cursor()
data = [[2], [6], [4]]
 
var = cursor.var(str, arraysize = len(data))


data[0].append(var)                               # OUT bind variable ':2'
cursor.executemany("""
        declare
            t_Num number := :1;
            t_OutValue varchar2(100);
        begin
            for i in 1..t_Num loop
                t_OutValue := t_OutValue || 'Y';
            end loop;
            :2 := t_OutValue;
        end;""", data)
 
#print("Result:", var.values)

#delete one

for parentId in (10, 20, 30):
    cursor.execute("delete from ChildTable where ParentId = :1",
            [parentId])
    print("Rows deleted for parent id", parentId, "are",
            cursor.rowcount)

#delete many

data = [[10], [20], [30]]
 
cursor.executemany("delete from ChildTable where ParentId = :1", data)
print("Rows deleted:", cursor.rowcount)
