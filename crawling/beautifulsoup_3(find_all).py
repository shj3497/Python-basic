from bs4 import BeautifulSoup

html = """
<html>
    <body>
       <ul>
        <li><a href="http://naver.com">naver</a></li>
        <li><a href="http://daum.net">daum</a></li>
       </ul>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all('a')  # a태그를 찾아라? >> 정답,  현재 a태그는 두개

for a in links:
    href = a.attrs['href'] # .attrs[] : a태그의 속성 href의 value를 반환
    text = a.string # .string : a태그안의 string값 반환
    print(text, ">", href)

lis = soup.find_all('li')   # 맞네.. li태그를 찾아라
for li in lis:
    print('<li> >>> : ', li)