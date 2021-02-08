import json
import xmltodict

### JSON 형식의 데이터 처리
# 딕셔너리

python_dict = {
    "이름":"홍길동",
    "나이":25,
    "거주지":"서울",
    "신체정보":{
        "키":175.4,
        "몸무게":71.2
    },
    "취미":[
        "등산",
        "자전거타기",
        "독서"
    ]
}
print(type(python_dict)) # dict
json_data = json.dumps(python_dict) # json.dumps(dict) >> .dumps() : json str형식으로 바꿔준다.
print(type(json_data)) # str
print(json_data) # 한글이 깨져서 나온다...
print()

json_data1 = json.dumps(python_dict, indent=3, sort_keys=True, ensure_ascii=False) # 흠..
print(json_data1)
json_dict1 = json.loads(json_data1)
print(type(json_dict1)) # dict
print(json_dict1['신체정보']['몸무게'])
print(json_dict1['취미']) # >>> JSON 데이터를 가지고 dictionary로 형 변환해서 key값으로 데이터를 출력하는 것
print(json_dict1['취미'][0])
print()

### XML 형식의 데이터 처리
xml_data = """<?xml version="1.0" encoding="UTF-8" ?>
    <사용자정보>
        <이름>홍길동</이름>
        <나이>25</나이>
        <거주지>서울</거주지>
        <신체정보>
            <키 unit="cm">175.4</키>
            <몸무게 unit="kg">71.2</몸무게>
        </신체정보>
        <취미>등산</취미>
        <취미>자전거타기</취미>
        <취미>독서</취미>
    </사용자정보>
"""
print(xml_data)
print()

dict_data = xmltodict.parse(xml_data, xml_attribs=True)
print(dict_data)
print()
print()
print(dict_data['사용자정보']['이름'])
print(dict_data['사용자정보']['신체정보'])
print(dict_data['사용자정보']['신체정보']['키']['@unit']) # 키의 속성 출력
print(dict_data['사용자정보']['신체정보']['키']['#text']) # 키의 텍스트 출력
print()
print()
dict_data1 = xmltodict.parse(xml_data)
user_name = dict_data1['사용자정보']['이름']
body_data = dict_data1['사용자정보']['신체정보']

# body_data['키'] : OrderedDict([('@unit', 'cm'), ('#text', '175.4')])
height = body_data['키']['#text']
height_unit = body_data['키']['@unit']

weight = body_data['몸무게']['#text']
weight_unit = body_data['몸무게']['@unit']

print("[사용자 {0}의 신체정보]".format(user_name))
print("* 키:{0}{1}".format(height, height_unit))
print("* 몸무게:{0}{1}".format(weight, weight_unit))
print()
print()

dict_data2 = xmltodict.parse(xml_data, xml_attribs=False) # xml형식의 데이터에서 지정했던 속성이 모두 무시되면서 딕셔너리 형식으로 변환
print(dict_data2)