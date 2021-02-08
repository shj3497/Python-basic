import os
import urllib
from urllib import request

from bs4 import BeautifulSoup

url = "http://kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "./file/forecast.xml"

if not os.path.exists(savename):
    request.urlretrieve(url, savename)

# 파일을 저장하고, 읽어 왔음 >> .read()로
xml = open(savename, 'r', encoding='utf-8').read()
# BeautifulSoup으로 코드를 얽어옴
soup = BeautifulSoup(xml,'html.parser')

# dictionary로 선언
info = {}

# xml파일에서
# find_all('location') : 모든 location 태그를 찾아라
for location in soup.find_all("location"):
    # xml파일에서
    # find('city') : city 태그명의 스트링 값을 name
    name = location.find('city').string
    # xml파일에서
    # find('wf') : wf 태그명의 스트링 값을 weather
    weather = location.find('wf').string
    if not (weather in info):
        info[weather] = [] # 공백으로 하겠다는건가?
    info[weather].append(name)
print(info)
for weather in info.keys():
    print("+", weather)
    for name in info[weather]:
        print(":", name)

print(info)