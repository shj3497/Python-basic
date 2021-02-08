"""
pandas는 구조적 데이터 표시와 처리하는 라이브러리이다.
구조적데이터 
    1차원배열 : Series() : 배열
    2차원배열 : DataFrame() : 행렬
pandas는 numpy 기반으로 만들어졌으며
복잡한 데이터 분석에 특화되어있다.

numpy 배열 : 자바의 배열
pandas 시리즈 : 자바의 list 성격

판다스는 금융권 데이터 분석으로 많이 사용된다.



Series를 활용한 데이터 생성
pandas.Series(seq_data)
    인덱스번호 자동입력되어 열로 입력된다.
    ex)
        pandas.Series(['a', numpy.nan, 1])
        0      a
        1    NaN
        2      1
        dtype: object
    numpy.nan = 데이터가 없음을 나타낸다.

pandas.Series(seq_data, index=index_data)
    인덱스번호도 컨트롤 가능


pandas.Series(dict_data)
    딕셔너리 데이터도 가능하다.
    ex)
        pandas.Series({'국어':100, '영어':95, '수학':90})
        key값이 index가 되고, value가 seq_data가 된다.


날짜 자동 생성 : data_range
pandas.date_range(start=None, end=None, periods=None, freq='D')


DataFrame을 활용한 데이터 생성
2차원 데이터 처리를위하여..
df = pandas.DataFrame(data [, index = index_data, columns = columns_data])
    ex)
        data : dictionary 라면
        columns = columns_list >> 딕셔너리의 키값
        columns_list의 순서를 변경해서 테이블을 구성할 수 있다.
        df.index : 인덱스 번호
        df.columns : 컬럼명
        df.values : 값들


pandas.Series() 의 연산
    ex)
        df1 = pandas.Series([1,2,3,4])
        df2 = pandas.Series([10,20,30,40,50])
        df1 + df2
        0    11.0
        1    22.0
        2    33.0
        3    44.0
        4     NaN
        dtype: float64   가능 >> 배열의 크기가 달라도 연산은 된다.
        데이터가 없는부분은 NaN으로 표시한다.

        a1 = numpy.array([1,2,3,4])
        a2 = numpy.array([10,20,30,40,50])
        a1 + a2 >> : 에러발생


pandas.DataFrame()의 연산
    ex)
        table_data3 = {'봄':[256.5,264.3,215.9,223.2,312.8],
                       '여름':[770.6,567.5,599.8,387.1,446.2],
                       '가을':[363.5,231.2,293.1,247.7,381.6],
                       '겨울':[139.3,59.9,76.9,109.1,108.1]}
        columns_list = ['봄','여름','가을','겨울']
        index_list = [2012,2013,2014,2015,2016]
        df8 = pandas.DataFrame(table_data3, index=index_list, columns=columns_list)

        ###############
        df8.mean() >> 컬럼별로 평균을 내준다.
        df8.mean(axis=1) >> 행별로 평균을 내준다.
        axis=0이 default이다.

        df8.describe() : 통계적 수치 전부 나타내준다.
        데이터수, 평균, 표준편차, 최솟값, 4분위수, 최댓값
        ###############


데이터를 원하는대로 선택하기
    DataFrame_data.head(n)
    ex)
        df.head() : 1행부터 default=5개를 뽑는다.
        df.tail() : 마지막행부터 defualt=5개를 뽑는다.
        df.head(3) : 1행부터 3개를 뽑는다.
        df.tail(2) : 마지막행부터 2개를 뽑는다.
    
    DataFrame_data[행_시작_위치 : 행_끝_위치]
    ex)
        df[2:4] : 2행부터 4행 전까지 뽑는다.

    DataFrame_data.loc[index_name]
    ex)
        df.loc['봄']
        df.loc['봄':'가을'] >> : 봄~가을 행을 출력한다.






"""
