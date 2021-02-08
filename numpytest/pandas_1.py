# 판다스

# s = pandas.Series(seq_data)
import numpy
import pandas

# ? numpy.array 는 행렬로 나오는데
# pandas.Series 는 열(?) 단위로 입력하는 느낌이랄까?
# 자동으로 index도 들어가네?
s1 = pandas.Series([10,20,30,40,50])
print(s1)
print()
print(s1.index)
print(s1.values) # 열단위로 입력되는 Series를 배열형태로 출력하려면 .values를 써줘야하네
print()

s2 = pandas.Series(['a','b','c',1,2,3])
print(s2) # dtype = object
a2 = numpy.array(['a','b','c',1,2,3])
print(a2.dtype) # dtype = unicode
print()

s3 = pandas.Series([numpy.nan,10,30]) # numpy.nan : Series데이터에 특정 원소가 없음을 나타낸다.
print(s3)

# s = pandas.Series(seq_data, index=index_seq)
# 오호.. 인덱스 번호마저도 컨트롤 가능하다는건가
index_date = ['2018-10-07', '2018-10-08', '2018-10-09', '2018-10-10']
s4 = pandas.Series([200, 195, numpy.nan, 205], index=index_date)
print(s4) # 맞네.. 인덱스번호도 컨트롤 가능
print()

# s = pandas.Series(dict_data)
# 딕셔너리로 넣으면 자동으로 인덱스 값이 key값이 되네,,
s5 = pandas.Series({'국어':100, '영어':95, '수학':90})
print(s5)
print()

# 날짜 자동생성 : data_range
# pandas.date_range(start=None, end=None, periods=None, freq='D')
data1 = pandas.date_range(start='2019.01.01', end='2019.01.07')
print(data1) # 어떤식으로 날짜를 입력하든 yyyy-mm-dd로 인식하네
data4 = pandas.date_range(start='2019-01-01', periods=7)
print(data4)
# panas.date_range() 함수의 freq 옵션
# D : 달력 날짜 기준 하루 주기
# B : 업무 날짜 기준 하루 주기 등...
data5 = pandas.date_range(start='2019-01-01', periods=4, freq='2D')
print(data5)
print()
index_date = pandas.date_range(start="2021-02-01", periods=5, freq='D')
data6 = pandas.Series([52,62,55,49,58], index=index_date)
print(data6)
print()

# DataFrame을 활용한 데이터 생성
# df = pandas.DataFrame(data [, index = index_data, columns = columns_data])
df1 = pandas.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(df1) # series와는 다르게 일반적으로 들어가네..
print()
data_list = numpy.array([[10,20,30],[40,50,60],[70,80,90]])
print("data_list \n", data_list)
df2 = pandas.DataFrame(data_list)
print(df2) # 확실이 2차원 배열 만들때는 pandas가 이쁘게 나옴
print()

# 운동 측정 데이터를 data_list2
# index_list2를 날짜?
# 로하면 각 날짜에 측정한 운동 데이터가 만들어 지겠군
data_list2 = numpy.array([[1,2,3],[4,5,6],[7,8,9],[10,11,11]])
index_date = pandas.date_range('2019-09-01', periods=4)
columns_list = ['A','B','C']
df3 = pandas.DataFrame(data_list2, index=index_date, columns=columns_list)
print(df3)
print()

table_data = {'연도':[2015,2016,2016,2017,2017],
              '지사':['한국','한국','미국','한국','미국'],
              '고객수':[200,250,450,300,500]}
print(table_data)
df4 = pandas.DataFrame(table_data)
print(df4)
print()
# columns = column_list 를 이용하여 dictionary의 키값을 가지고 순서를 지정해 줄수 있다.
df5 = pandas.DataFrame(table_data, columns=['연도','지사','고객수'])
print(df5)
print()
print(df5.index) # >>> : RangeIndex(start=0, stop=5, step=1)
print(df5.columns) # >>> : Index(['연도', '지사', '고객수'], dtype='object')
print(df5.values)
# Index(['연도', '지사', '고객수'], dtype='object')
# [[2015 '한국' 200]
#  [2016 '한국' 250]
#  [2016 '미국' 450]
#  [2017 '한국' 300]
#  [2017 '미국' 500]]

print()
s1 = pandas.Series([1,2,3,4,5])
s2 = pandas.Series([10,20,30,40,50])
print(s1+s2)
print(s2-s1)
print(s1*s2)
print(s2/s1)
print()
s3 = pandas.Series([1,2,3,4])
s4 = pandas.Series([10,20,30,40,50])
print(s3+s4) # 배열크기가 다른경우에도 연산은 가능하다. 단 NaN으로 뜬다.
a1 = numpy.array([1,2,3,4])
a2 = numpy.array([10,20,30,40,50])
# print(a1+a2) # numpy는 배열크기가 다를경우 에러를 발생시킨다.
print()
print()

table_data1 = {'A':[1,2,3,4,5],
               'B':[10,20,30,40,50],
               'C':[100,200,300,400,500]}
df6 = pandas.DataFrame(table_data1)
print(df6)
table_data2 = {'A':[6,7,8],
               'B':[60,70,80],
               'C':[600,700,800]}
df7 = pandas.DataFrame(table_data2)
print(df7)
print(df6+df7)
print()

table_data3 = {'봄':[256.5,264.3,215.9,223.2,312.8],
               '여름':[770.6,567.5,599.8,387.1,446.2],
               '가을':[363.5,231.2,293.1,247.7,381.6],
               '겨울':[139.3,59.9,76.9,109.1,108.1]}
columns_list = ['봄','여름','가을','겨울']
index_list = [2012,2013,2014,2015,2016]
df8 = pandas.DataFrame(table_data3, index=index_list, columns=columns_list)
print(df8)
print("평균")
print(df8.mean()) # ??! DataFrame은 컬럼값을 기준으로 평균, 표준편차, 분산 다 가능
print("표준편차")
print(df8.std())
print("분산")
print(df8.var())
print()
print(df8.mean(axis=1)) # axis=0 이 default임 , axi1=1이면 행으로도 연산이 가능하다.
print("describe()")
print(df8.describe()) # 와... 충격적인데?
# 일반적인 통계적 수치를 다 나타내준다.
print()

# 데이터를 원하는대로 선택하기
KTX_data = {'경부선KTX':[39060, 39896, 42005, 43621, 41702, 41266, 32427],
            '호남선KTX':[7313, 6967, 6373, 6626, 8675, 10622, 9228],
            '경전선KTX':[3627, 4168, 4088, 4424, 4606, 4984, 5570],
            '전라선KTX':[309, 1771, 1954, 2244, 3146, 2945, 5766],
            '동해선KTX':[numpy.nan, numpy.nan, numpy.nan, numpy.nan, 2395,3786,6667]}
col_list = ['경부선KTX','호남선KTX','경전선KTX','전라선KTX','동해선KTX']
index_list = ['2011','2012','2013','2014','2015','2016','2017']
df_KTX = pandas.DataFrame(KTX_data, columns=col_list, index=index_list)
print(df_KTX)

# DataFrame_data.head(n) , .tail(n)
print(df_KTX.head()) # default = 5이다. .head() : 1행부터
print(df_KTX.tail()) # default = 5이다. .tail() : 마지막 행부터
print(df_KTX.head(3))
print(df_KTX.tail(2))
print()

# DataFrame_data[행_시작위치 : 행_끝위치]
print(df_KTX[1:3])
print()

# DataFrame_data.loc[index_name]
# 행데이터를 뽑아온다.
print(df_KTX.loc['2011'])
print(df_KTX.loc['2013':'2016']) # ? 2016도 출력되네?
print()

# DataFrame_data[column_name]
# 지정한 열 데이터를 뽑아온다.
print(df_KTX['경부선KTX'])
print()

# DataFrame_data[column_name][start_index_name : end_index_name]
# DataFrame_data[column_name][start_index_pos : end_index_pos]
# 열데이터를 지정해서 원하는 만큼의 행을 뽑아온다.
print(df_KTX['경부선KTX']['2012':'2014']) # 키를 지정하면 12~14년출력
print(df_KTX['경부선KTX'][2:5]) # 인덱스로 하면 2~4까지 출력 13~15년