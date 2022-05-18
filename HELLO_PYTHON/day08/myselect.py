import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='python', port=3305, db='python', charset='utf8')
cur = conn.cursor()

sql = "select * from emp"
cur.execute(sql)

rows = cur.fetchall()

for i in rows:
    print(i[0],i[1],i[2],i[3])
# print(rows)

cur.close()
conn.close()