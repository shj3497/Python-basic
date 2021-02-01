import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src,'html.parser')

links = soup.select('a')
print(len(links))
print("\n")

print(links[:3])
print("\n")

external_links = soup.select('a[class = "external text"]')
print(external_links[:3])
print("\n")

# id값이 siteNotice 인것을 출력
id_selector = soup.select('#siteNotice')
print(id_selector)
print("\n")

# div태그의 id값이 siteNotice인 것을 출력
id_selector2 = soup.select('div#siteNotice')
print(id_selector2)
print("\n")

# 해당하는 p태그의 id값이 siteNotice인 태그가 없다.
id_selector3 = soup.select('p#siteNotice')
print(id_selector3)
print("\n")

# class속성 값이 mw-headline 인 태그를 모조리 출력
class_selector = soup.select('.mw-headline')
print(class_selector)
print("\n")

# span태그에 class속성 값이 mw-headline인 것을 출력
class_selector2 = soup.select('span.mw-headline')
print(class_selector2)