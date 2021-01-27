import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss2.jsp"

values = {
    'stnId':'108'
}
params = urllib.parse.urlencode(values)
url = API +"?"+ params
print("url >>> : ", url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)

# 저장하기 위한단계
# urllib.request.urlretrieve(url주소, 저장장소와 이름)
savename="./data/weather.xml"
urllib.request.urlretrieve(url, savename)
print("저장되었습니다.")