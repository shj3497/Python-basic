from bs4 import BeautifulSoup
from pip._vendor import requests

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url) # html 응답코드 반환
print(resp)
html_src = resp.text

soup = BeautifulSoup(html_src,'html.parser')

target_img = soup.find(name='img', attrs={'alt': 'Seoul-Metro-2004-20070722.jpg'})
print('HTML 요소: ', target_img)
print("\n")

# 원하는 <img>태그를 추출하고 난 후 src(이미지 파일 주소)를 받아온다.
target_img_src = target_img.get('src')
print(target_img_src)
print("\n")

target_img_resp = requests.get('http:' + target_img_src)
print("target_img_resp : ", target_img_resp)
out_file_path = "./data/download_image.jpg"

# with open(out_file_path, 'wb') as out_file:
# open : 파일을 오픈한다. >> close()를 해야한다, 파이썬을 닫으면 자동 close()
# with open : open() 후 자동으로 close()를 해준다.
# out_file_path : 파일이 저장되어있는 위치
# 'wb' : 파일 모드
#           열기(r), 쓰기(w or x), 추가(a), 수정(+)
#           w : 파일이 이미 있으면 그 내용을 삭제하고 새로 생성
#           x : 파일이 이미 있으면 FileExistsError를 발생시킨다.
#           텍스트파일(t), 바이너리 파일(b)를 지정할 수 있다.
# .read() : 읽기
# with open
with open(out_file_path, 'wb') as out_file:
    out_file.write(target_img_resp.content) # 이미지 파일이라 파일의 주소명.content 로 write 해줌
    print("이미지 파일로 저장하였습니다.")