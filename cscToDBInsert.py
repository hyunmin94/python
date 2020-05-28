import csv
import pymysql
# 컬럼데이터를 Date 타입으로 변환하기 위해 datetime 모듈인포트
# import datetime

config ={'host':'127.0.0.1',
         'port':3306,
         'user':'root',
         'password':'hyunmin',
         'db':'testdb'}

conn = pymysql.connect(**config)

try:
    cur = conn.cursor()

    file = csv.reader(open('C:\\myPyCode\PycharmProjects\input.csv','r'))

    header = next(file)

    delSQL = 'delete from suppliers;'
    cur.execute(delSQL)

    for row in file:
        # Date 타입으로 변환 후 데이터 삽입
        # print(row)
        # row[4] = datetime.datetime.strptime(row[4],'%Y-%m-%d')

        sql = 'insert into suppliers values(%s,%s,%s,%s,%s)'
        cur.execute(sql, row)

    conn.commit()

finally:
    conn.close()