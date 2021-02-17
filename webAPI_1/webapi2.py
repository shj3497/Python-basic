import requests

req_url = "http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getTMStdrCrdnt"
API_KEY = "ghN%2FQYdn8YfoEgKmKyJwojm2F6AhNVvJXlWFDWd9gWOGPW31EJIMNwVgTvZDqb%2B2pYLPWGk0Tc4oMIFNtwJu%2FA%3D%3D"
API_KEY_decode = requests.utils.unquote(API_KEY)
print(API_KEY_decode)

umd_name = "논현동"
num_of_rows = 10
page_no = 1

output_type="json"

req_parameter = {
    "ServiceKey":API_KEY_decode,
    "umdName":umd_name,
    "pageNo":page_no,
    "numOfRows":num_of_rows,
    "_returnType":output_type
}
dict_data = requests.get(req_url, params=req_parameter).json()
print(dict_data) # 출력 결과물 JSON데이터 조회
print(dict_data['totalCount'])

print("[입력한 읍/면/동명]", umd_name)
print("[TM 기준 좌표 조회 결과]")

for k in range(dict_data['totalCount']):
    sido = dict_data['list'][k]['sidoName'] # list라는 키값에 두개의 배열이있다.
    sgg = dict_data['list'][k]['sggName']
    umd = dict_data['list'][k]['umdName']
    tmX = dict_data['list'][k]['tmX']
    tmY = dict_data['list'][k]['tmY']

    print("-위치 : {0} {1} {2}".format(sido, sgg, umd))
    print("- k ={0}, TM좌표(X,Y) : {1},{2} \n".format(k, tmX, tmY))