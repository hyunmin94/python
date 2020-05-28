import csv
import pymysql

config ={'host':'127.0.0.1',
         'port':3306,
         'user':'root',
         'password':'hyunmin',
         'db':'testdb'}

conn = pymysql.connect(**config)

try:

    sql = 'select * from suppliers;'
    cur = conn.cursor()
    cur.execute(sql)

    file = csv.writer(open('C:\\myPyCode\PycharmProjects\input.csv','w'), delimiter = ',')

    file.writerow(['Supplier_Name','Invoice_Number','Part_Number','Cost','Purchase_Date'])

    for data in cur:
        file.writerow(data)

finally:
    conn.close()