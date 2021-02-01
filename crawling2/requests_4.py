from bs4 import BeautifulSoup
from pip._vendor import requests

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')
print(type(soup))
print("\n")

print(soup.head)
print("\n")
print(soup.body)
print("\n")

# soup : BeautifulSoup : url주소의 소스코드 html코드를 읽어올수 있음
# soup.title : .html의 <title>태그를 불러온다.
# soup.title.name : 태그명?
# soup.title.string : <title> 태그의 value
print('title 태그 요소 >>> : ', soup.title)
print('title 태그 이름 >>> : ', soup.title.name)
print('title 태그 문자열 >>> : ', soup.title.string)
