import json

import requests

"""
    RESTful(Representational State Transfer) : 레스트 풀
    	http://www.abc.com/aaa/bbb.jsp?key=value&key=value&key=인증키
    	GET 방식 : 인증키로 인증해서 데이터를 요청하고 받는 방식
    	    URI : 아이덴티파이어 식별자로 데이터를 요청하고 응답 받음
    	    POST : POST를 통해 해당 URI를 요청하면 리소스를 생성합니다.
    	    GET : GET을 통해

    SOAP(Simple Object Access Protocol) : 숲
        POST 방식
        body 부분에 데이터를 첨부하여 보내는 방식

"""
apikey = "073225bb1af783fa264ee484a37f07c4"
cities = ["Seoul,KR", "Tokyo,JP","New York,US"]
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

print(api)
# 켈빈 온도를 섭씨 온도로 변환하는 함수
k2c = lambda k: k-273.15
print(k2c)
for name in cities:
    url = api.format(city=name, key=apikey)
    resp = requests.get(url)
    print(resp)
    print(resp.text)

# JSON 타입을 python에서는 딕셔너리라고 봐도 될듯
for name in cities:
    url = api.format(city=name, key=apikey)
    resp = requests.get(url)
    print(resp)
    data = json.loads(resp.text)
    print("+ 도시 =", data["name"])
    print(": 날씨 =", data["weather"][0]["description"]) 
    # >> key값이 weather인 value를 보면 배열로 이루어져있다.
    # >> seoul의 경우 배열이 하나만 있지만, 미국의 경우 배열 길이가 2임
    # 그래서 data["weather"][0]으로 한개만 불러서 써줌
    print(": 최저 기온 =", k2c(data["main"]["temp_min"]))
    print(": 최고 기온 =", k2c(data["main"]["temp_max"]))
    print(": 습도 =", data["main"]["humidity"])
    print(": 기압 =", data["main"]["pressure"])
    print(": 풍향 =", data["wind"]["deg"])
    print(": 풍속 =", data["wind"]["speed"])
    print("")
