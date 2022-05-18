import pymysql

conn = None
cur = None

e_id = ""
e_name = ""
sex = ""
addr = ""

sql=""

conn = pymysql.connect(host='127.0.0.1', user='root', password='python', port=3305, db='python', charset='utf8')
cur = conn.cursor()

while(True):
    e_id = input("사용자 ID를 입력하세요(엔터 클릭시 종료) : ")
    if e_id == "":
        break;
    e_name = input("사용자 이름을 입력하세요 : ")
    sex = input("사용자 성별을 입력하세요 : ")
    addr = input("사용자 주소를 입력하세요 : ")
    sql = "INSERT INTO EMP VALUES('" + e_id + "','" + e_name + "','" + sex + "','" + addr + "')"
    cur.execute(sql)

conn.commit()

conn.close()

#================================================================================

# STEP 1
import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8') # 한글처리 (charset = 'utf8')
 
# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor(pymysql.cursors.DictCursor)
 
# STEP 4: SQL문 실행 및 Fetch
sql = """insert into emp(e_id,e_name,sex,addr) 
         values(%s,%s,%s,%s)"""
         
cur.execute(sql,(3,'3','3','3'))
con.commit() 
 
# 데이타 Fetch
#rows = cur.fetchall()

#print(rows)     # 전체 rows

cur.close();
# STEP 5: DB 연결 종료
con.close()