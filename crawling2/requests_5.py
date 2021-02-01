from bs4 import BeautifulSoup
from pip._vendor import requests

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, "html.parser")

# soup.findAll(name="img") 모든 이미지 태그를 찾는다.
first_img = soup.find(name='img')
print(first_img)
print("\n")

# <img>태그의 alt는 alternate '대체하다' 로
# 일반적으로는 src로 이미지 파일의 경로만 표시해주는데
# alt 속성으로 그림의 설명을 적어주는데 쓰인다.
# <img> 태그에 항상 alt를 써주는 노력을 해야한다.
# 아래 코드를 보면 name='img' 이미지 태그를 찾고,
# attr={'alt':'...'} 는 alt 속성에서 ...내용인 <img>태그를 찾으라는 의미
target_img = soup.find(name='img', attrs={'alt' : 'Seoul-Metro-2004-20070722.jpg'})
print(target_img)