# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
from bs4 import BeautifulSoup
from day12.dao_blog import DaoBlog

blog = DaoBlog()

client_id = "aRSCUwSHcrCv1a7ZKwPn"
client_secret = "b21nx5tenz"
encText = urllib.parse.quote("오류동맛집")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
response_body = response.read()
text = response_body.decode('utf-8')

soup = BeautifulSoup(text, "xml")
items = soup.select("item")
for i in items:
    title = i.select_one("title").text.replace("'","&#39;")
    link = i.select_one("link").text.replace("'","&#39;")
    description = i.select_one("description").text.replace("'","&#39;")
    bloggername = i.select_one("bloggername").text.replace("'","&#39;")
    bloggerlink = i.select_one("bloggerlink").text.replace("'","&#39;")
    postdate = i.select_one("postdate").text.replace("'","&#39;")
    cnt = blog.myinsert(title,link,description,bloggername,bloggerlink,postdate)
    print("cnt",cnt)
    
    
    