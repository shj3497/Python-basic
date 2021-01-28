from pip._vendor import requests

url = "https://www.python.org/"
resp = requests.get(url)
# print(resp) page 요청에 대한 응답번호가 뜬다.
html = resp.text # 그 응답번호에대한 .text로 요청을 하면 페이지의 html내용들이 출력된다.
print(html)