import re

import pandas
import requests
from bs4 import BeautifulSoup

# 위키피디아 미국 ETF 웹 페이지에서 필요한 정보를 스크래핑하여 딕셔너리 형태로 변수 etfs에 저장
url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
resp = requests.get(url)
# print(resp.text) url에서 긁어온 html 코드

soup = BeautifulSoup(resp.text, 'lxml')
# print(soup)

rows = soup.select("div > ul > li")
# print("rows >>> : ", rows)

etfs = {} # 딕셔너리 선언
for row in rows:
    try:
        etf_name = re.findall('^(.*) \(NYSE', row.text)
        etf_market = re.findall('\((.*)\|', row.text)
        etf_ticker = re.findall('NYSE Arca\|(.*)\)', row.text)
        if (len(etf_ticker) > 0) & (len(etf_market) > 0) & (len(etf_name) > 0):
            etfs[etf_ticker[0]] = [etf_market[0], etf_name[0]]

    except AttributeError as err:
        pass

# etfs 딕셔너리 출력
print(etfs)
print("\n")

# etfs 딕셔너리를 데이터 프레임으로 변환
df = pandas.DataFrame(etfs)
print(df)