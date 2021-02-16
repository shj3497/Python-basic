import pandas

# 파일 경로를 찾고, 변수를 file_path에 저장한다.
file_path = "./data/read_csv_sample.csv"

# read_csv() 함수로 데이터 프레임 변환. 변수 df1에 저장
df1 = pandas.read_csv(file_path)

print(df1)
print("\n")

# read_csv() 함수로 데이터 프레임 변환. 변수 df2에 저장. header=None 옵셥
df2 = pandas.read_csv(file_path, header=None)
print(df2)
print("\n")

# read_csv() 함수로 데이터 프레임 변환. 변수 df3에 저장. index_col=None 옵션
df3 = pandas.read_csv(file_path, index_col=None)
print(df3)

# read_csv() 함수로 데이터 프레임 변환. 변수 df4에 저장. index_col='c0' 옵션
df4 = pandas.read_csv(file_path, index_col='c0')
print(df4)