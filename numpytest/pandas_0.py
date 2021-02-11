"""
pandas는 구조적 데이터 표시와 처리하는 라이브러리이다.
구조적데이터 
    1차원배열 : Series() : 배열    : 문자, 숫자 등 여러가지 데이터 타입가능
             <-> numpy.array : 데이터타입이 하나로 바뀐다. ex) 2, 1.0 >> 2.0, 2.0 모두 실수타입
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

    DataFrame_data.loc[index_name][column_name] >>> .loc !!
    DataFrame_data.loc[index_name, column_name]
    DataFrame_data[column_name].loc[index_name]
    DataFrame_data[column_name][index_name]
    DataFrame_data[column_name][index_pos]
        >> : 일반적 조회 : 행,열
        >> : .loc : 열,행

데이터 통합하기
세로방향으로 통합하기 : .append() : 행데이터 삽입
    DataFrame_data1.append(DataFrame_data2 [, ignore_index=True])
        df1.append(df2) 는 인덱스번호가 같으면 중복된다.
        ignore_index=True 를 하게되면 df1에 따라 인덱스번호가 순차적으로 증가한다.

가로방향으로 통합하기 : .join() : 열데이터 삽입
    DataFrame_data1.join(DataFrame_data2)
        >> : 열데이터가 삽입된다. append()와는 반대

특정 열을 기준으로 통합하기 : .merge()
DataFrame_left_data.merge(DataFrame_right_data, how=merge_method, on=key_label)
    how 선택인자
        left : 왼쪽 데이터는 모두 선택하고 지정된 열(key)에 값이 있는 오른쪽 데이터를 선택
             : .merge()를 기준으로 왼쪽에 있는(DataFrame_left_data) key값을 선택 (
        right : 오른쪽 데이터는 모두 선택하고 지정된 열(key)에 값이 있는 왼쪽 데이터를 선택
              : .merge()를 기준으로 오른쪽에 있는(DataFrame_right_data) key 값을 선택
        outer : 지정된 열(key)을 기준으로 왼쪽과 오른쪽 데이터를 모두 선택
              : key값을 합하여 모든 데이터를 표시한다. (합집합 느낌)
        inner : 지정된 열(key)을 기준으로 왼쪽과 오른쪽 데이터중 공통항목만 선택(default)
              : key값이 일치한 데이터만 표시 (교집합 느낌)
    on
        공통 키 선택


데이터 파일을 읽고 쓰기
표 형식의 데이터 파일을 읽기
    DataFrame_data = pandas.read_csv(file_name [, options])
        options
            encoding="UTF-8"
            sep = " " >> : csv파일이 ',' 구분자가 아닌 'space(띄어쓰기)'로 구분되어 있을경우
            index_col = "컬럼명"




"""
