import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='hyunmin',
                       db='testdb')

sql = "SELECT empno, ename, sal, job, deptno FROM emp"

cur = conn.cursor()
cur.execute(sql)
# 출력 결과의 상위 3개 레코드만 호출
for data in cur.fetchmany(3):
    print(data)

conn.close()
