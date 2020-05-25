import pymysql

conn = pymysql.connect(host = '127.0.0.1', port=3306,
                       user ='root',password='hyunmin')

if conn.open:
    with conn.cursor() as curs:
        print("connected")

conn.close()
