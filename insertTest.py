import MySQLdb

config ={'host':'127.0.0.1',
         'port':3306,
         'user':'root',
         'password':'hyunmin',
         'db':'testdb'}

conn = MySQLdb.connect(**config)
cur = conn.cursor()

v_empno = 5
v_ename = "Johnson"
v_sal = 1500

sql = "insert into emp(empno, ename, sal, hiredate) values(%s, %s, %s, now())"
sql_data = (str(v_empno), v_ename, str(v_sal))

cur.execute(sql, sql_data)
conn.commit()
conn.close()
