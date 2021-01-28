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

with open(frame, "w", encoding="utf-8") as f:
    f.write(price)