import urllib.request as req

from bs4 import BeautifulSoup

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

# .find('') : 태그를 찾아간다.
# .find(id='') : id값을 찾아간다.

title = soup.find("title").string   # 태그 이름이 title인 태그안의 내용을 저장
wf = soup.find('wf').string         # _2에서는 태그자체를 저장해주고 print에서 .string으로 태그안에있는 내용을
print(title)                        # 출력했지만 지금은 태그안에있는 내용을 변수로 입력받았다.
print(wf)
