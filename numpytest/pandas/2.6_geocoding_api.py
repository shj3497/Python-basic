import googlemaps
import pandas

my_key = "AIzaSyDuLl7Dn2sYpcqjiyzlTgDc2iNcKQ0n3A4";

# 구글 맵스 객체 생성하기
maps = googlemaps.Client(key=my_key) # me_key값 입력

lat = [] # 위도
lng = [] # 경도

# 장소(또는 주소) 라스트
places = ["서울시청", "국립국악원", "해운대해수욕장", "독산동331-44"]

i = 0
for place in places:
    i = i+1
    try:
        print(i, place)
        # 지오코딩 API 결과값 호출하여 geo_location 변수에 저장
        geo_location = maps.geocode(place)[0].get("geometry")
        print("geo_location >>> : ", geo_location)
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])

    except:
        lat.append("")
        lng.append("")
        print(i)

# 데이터 프레임으로 변환하기
df = pandas.DataFrame({'위도':lat, '경도':lng}, index=places)
print("\n")
print(df)