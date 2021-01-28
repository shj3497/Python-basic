
import urllib.request as req

from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
print("url >>> : ", url)
print()

res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

price = soup.select_one("div.head_info > span.value").string
won = soup.select_one("div.head_info > span.txt_krw > span.blind").string
print("usd/krw = ", price, won)
