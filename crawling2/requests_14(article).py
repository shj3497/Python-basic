import datetime
import urllib.request

from bs4 import BeautifulSoup
from pip._vendor import requests

url='https://news.daum.net/'
resp = requests.get(url)
print(resp)
html_src = resp.text
f = open('./data/'+str(datetime.date.today())+'_articles.txt', 'w', encoding="utf-8")
#soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
soup = BeautifulSoup(html_src, 'html.parser')
# class 이름이 thumb_relate인 것들을 배열로 만듬
for i in soup.find_all('div', {'class' : "thumb_relate"}):
    try:
        # f : 위에서 open() 함수로 선언된 url주소, 쓰기방법, 파일이름, 인코딩방법으로
        # .write() : 파일에 쓴다.
        # i.text : html에 기술된 내용 긁어옴
        f.write(i.text + '\n')
        # i.find_all('a')[0].get('href') : <a href>를 긁어온다.
        f.write(i.find_all('a')[0].get('href')+'\n')
        # 위에서 <a href>로 받아온 url에 접속하여
        # <p> 태그의 내용들을 쓴다.
        soup2 = BeautifulSoup(urllib.request.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
        for j in soup2.find_all('p'):
            f.write(j.text)
    except:
        pass
f.close()
