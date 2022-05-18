import pymysql

con = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8') # 한글처리 (charset = 'utf8')
 
cur = con.cursor()
e_id = "3"
e_name = "4"
sex = "4"
addr = "4"

sql = f"""
         update emp
         set e_name='{e_name}',
         sex='{sex}',
         addr='{addr}'
         where
         e_id='{e_id}'
         """
         
cnt = cur.execute(sql)
con.commit() 

cur.close();

con.close()