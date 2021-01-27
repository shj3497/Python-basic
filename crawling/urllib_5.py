import sys
import urllib.request as req
import urllib.parse as parse
# 파이썬 명령행 인수 108
# 전국 : 108
# 서울/경기 109
# 강원도 105
# 충북 131
# 충남 133
# 전북 146
# 전남 156
# 경북 143
# 경남 159
# 제주 184

# 파이썬 명령행 인수를 받기 위해서
# sys.argv로 입력을 받는다.
if len(sys.argv) <=1:
    print("USAGE: download-forecasg-argv <Region Number>")
    sys.exit()
# 마우스 우클릭하여 Modify Run Configuration을 들어가보면
# parameters에 값을 넣을 수 있다.
regionNumber = sys.argv[1]

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': regionNumber
}
params = parse.urlencode(values)
url = API +"?"+ params

# urllib.request.urlopen(url) : 페이지 요청
# urllib.request.urlopen(url).read() : 페이지를 읽어온다.
# urllib.request.urlopen(url).decode('utf-8') : 요청한 페이지를 decode 한다.
data = req.urlopen(url).read()
text = data.decode('utf-8')
print(text)