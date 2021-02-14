import pandas

# 판다스 DataFrame() 함수로 데이터 프레임 변환. 변수 df에 저장
data = {'name' : [ 'Jerry', 'Riah', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"],
        }
df = pandas.DataFrame(data)
df.set_index('name', inplace=True) # 열 인덱스를 name 로 지정
print(df)

# to_csv() 메소드를 사용하여 csv 파일로 내보낼수 있다.
df.to_csv("./data/df_sample.csv")

