import pymysql
class DaoBlog:
    def __init__(self):
        self.con = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8') # 한글처리 (charset = 'utf8')
 
        self.curs = self.con.cursor(pymysql.cursors.DictCursor)
   
    def myinsert(self,title,link,description,bloggername,bloggerlink,postdate):
        sql = f"""
            insert into blog(title,link,description,bloggername,bloggerlink,postdate) 
                values(
                '{title}','{link}','{description}','{bloggername}','{bloggerlink}','{postdate}')
        """
        cnt = self.curs.execute(sql)
        self.con.commit() 
        return cnt
   
if __name__ == '__main__':
    de = DaoBlog()
    emp = de.myinsert(6)
    print("emp",emp) 