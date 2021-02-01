import urllib.request

from bs4 import BeautifulSoup

url = "https://m.stock.naver.com/marketindex/index.nhn"
res = urllib.request.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

# price = soup.select_one("div.head_info > span.value").string
# div 태그의 속성 head_info > 자식태그가 span이고 속성이 value인 값을 받아옴
# print("usd/krw=", price);

print(type(soup))
print("\n")

print(soup.head)
print(soup.body)

print('title 태그 요소: ', soup.title)
print('title 태그 이름: ', soup.title.name)
print('title 태그 문자열: ', soup.title.string)