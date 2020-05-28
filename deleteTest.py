import MySQLdb

config ={'host':'127.0.0.1',
         'port':3306,
         'user':'root',
         'password':'hyunmin',
         'db':'testdb'}

conn = MySQLdb.connect(**config)
cur = conn.cursor()

sql = "delete from emp where empno = 1 or empno = 5"

cur.execute(sql)
conn.commit()
conn.close()