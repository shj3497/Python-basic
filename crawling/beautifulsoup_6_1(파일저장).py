import datetime
import urllib.request as req

from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"

res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

price = soup.select_one("div.head_info > span.value").string
print("usd/krw = ", price)
#################################################################
t = datetime.date.today()
frame = "./data/" + t.strftime("%Y-%m-%d")+".txt"

# with open() : open()이 종료되면 자동으로 close()된다.
# open() 만 사용하면 따로 close()를 해주어야한다.
# "w" : 쓰기만적용 : 이미 파일이 존재하면 현재파일 없애고 새로 파일을 만든다.
# <-> "x" : 이미 같은 이름의 파일이 존재하면 에러 발생
with open(frame, "w", encoding="utf-8") as f:
    f.write(price)