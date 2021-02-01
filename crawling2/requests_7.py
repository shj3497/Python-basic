from bs4 import BeautifulSoup
import re

from pip._vendor import requests

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src,'html.parser')

links = soup.find_all('a')
print("하이퍼 링크 개수 : ", len(links))
print("\n")
print("첫 3개의 원소 : ", links[:3])
print("\n")

wiki_links = soup.find_all(name='a', href=re.compile("/wiki/"), limit=3)
print("/wiki/ 문자열이 포함된 하이퍼링크: ", wiki_links)
print("\n")

# soup.find_all(name="a", : a태그 모두를 찾고
# attrs={"class":"external text"} : 속성들중 class 속성이름이 external text를 찾는다.
# limit = 3 : 3개까지만
external_links = soup.find_all(name="a", attrs={"class": "external text"}, limit=3)
print("class 속성으로 추출한 하이퍼링크: ", external_links)