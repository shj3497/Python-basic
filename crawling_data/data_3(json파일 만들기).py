import json
import os
from urllib import request

url = "https://api.github.com/repositories"
savename = "./file/repo.json"

# 여기가 저장과정..
# urllib.request.urlretrieve(url주소, 저장장소와 이름)
if not os.path.exists(savename):
    request.urlretrieve(url, savename)

# open('r') : 파일을 여는 역할
# .read() : 파일을 읽는 역할
items = json.load(open(savename,'r',encoding='utf-8'))

# s = open(savename, "r", encoding="utf-8").read()
# items = json.load(s)
# print(items)

for item in items:
    # item["owner"]["login"] : 딕셔너리안에 키:딕셔너리로 저장되어있어서
    # 호출 하는 방법이 key:owner로 value:딕셔너리를 호출하고,
    # key:login으로 value를 호출한다.
    print(item["name"] + "_" + item["owner"]["login"])
