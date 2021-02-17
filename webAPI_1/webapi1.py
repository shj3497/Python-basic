import datetime

import requests

API_KEY = "ghN%2FQYdn8YfoEgKmKyJwojm2F6AhNVvJXlWFDWd9gWOGPW31EJIMNwVgTvZDqb%2B2pYLPWGk0Tc4oMIFNtwJu%2FA%3D%3D";
API_KEY_decode = requests.utils.unquote(API_KEY)
print(API_KEY_decode)

# [날짜 및 시간 설정]
now = datetime.datetime.now()

# baseDate에 날짜를 입력하기 위해 날짜 출력 형식을 지정해 변수에 할당한다.
date = "{:%H00}".format(now)

# 현재 분이 30분 이전이면 이전 시간 정시를 설정
if(now.minute >=30):
    time="{0}00".format(now.hour)
else:
    time="{0}00".format(now.hour-1)

# [요청 주소 및 요청 변수 지정]
req_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService"

baseDate = date
baseTime = time

nx_val = 60
ny_val = 127

num_of_rows = 6
page_no = 1
output_type="JSON"

req_parameter = {
    "ServiceKey":API_KEY_decode,
    "pageNo":page_no,
    "numOfRows":num_of_rows,
    "dataType":output_type,
    "base_date":"20210217",
    "base_time":"0500",
    "nx":"1",
    "ny":"1"
}

# [데이터 요청]
r = requests.get(req_url, params=req_parameter)
print(r)
dict_data = r.json()
print(dict_data)