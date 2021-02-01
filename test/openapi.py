from urllib.parse import unquote, urlencode, quote_plus

import requests
from bs4 import BeautifulSoup
params = "&testYm=201912"
My_API_Key = "xOCGwswCTZxu4E3QrSfdCm9mZz2H59Bf4h7G%2FLBHyWbyfzuDI50MjIkOFZDZEmFW4KknKJDr0cmSPQn0k9RRDA%3D%3D"
open_url = "http://www.kspo.or.kr/openapi/service/nfaTestInfoService/getNfaTestRsltList?serviceKey="+My_API_Key+params
print(open_url)
res = requests.get(open_url)
print(res)
soup = BeautifulSoup(res.content, 'html.parser')
print(soup)
