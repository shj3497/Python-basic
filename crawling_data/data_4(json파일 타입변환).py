import json

price = {
    "data": "2021-01-24",
    "price": {
        "Apple": 80,
        "Orange": 55,
        "Banana": 40
    }}
# price는 딕셔너리 구조이다.
# json.dumps() 함수는 Python에서 dictionary 구조를
# 스트링 객체로 바꿔준다.
s = json.dumps(price)
print(s)
print(type(s))

print(price)
print(type(price))