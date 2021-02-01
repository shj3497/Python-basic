from pip._vendor import requests

url = "https://www.python.org/"
resp = requests.get(url) # html의 응답 코드를 반환한다.
print("1", resp)

url2 = "https://www.python.org/1"
resp2 = requests.get(url2)  # html의 응답 코드를 반환
print("2", resp2)           # 없는 주소이므로 404를 반환 할 것이다.