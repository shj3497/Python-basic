import pandas

# HTML 파일 경로 or 웹 페이지 주소를 url 변수에 저장
url = "./data/sample.html"

# HTML 웹페이지의 표(table)을 가져와서 데이터 프레임으로 변환
tables = pandas.read_html(url)
print(tables)

# 표(table)의 개수 확인
print(len(tables)) # unnamed: 0 라고 출력되는것은 <td>에 아무것도 없기때문에 그렇다.
# thead 와 tbody가 따로 구분되어 출력된다.

print()

# tables 리스트의 원소를 iteration 하면서 각각 화면 출력
for i in range(len(tables)):
    print("tables[%s]" %i)
    print(tables[i])
    print("\n")

# 파이썬 패키지 정보가 들어있는 두번째 데이터 프레임을 선택하여 df변수에 저장
df = tables[1]
print(df)
print("\n")

# 'name'열을 인덱스로 지정
df.set_index(['name'], inplace=True)
print(df)