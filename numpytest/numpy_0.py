"""
시퀀스 데이터로부터 배열 생성
arr_obj = numpy.array(seq_data)
    seq_data = 배열

범위를 지정해 배열 생성
arr_obj = numpy.arange([start,] stop[, step])
    [] : 생략가능
    ex) numpy.arange(0, 10, 2)
        >> [0,2,4,6,8]

2차원 배열 생성
arr_obj = numpy.arange(stop).reshape(m,n)
    stop : 0 ~ stop 까지의 숫자
    .reshape(x,y) : m * n 행렬로 만든다.
    ex) numpy.arange(12).reshape(4,3)    
a1 = arr_obj.shape
     .shape : 행렬의 구조 확인

시작과 끝을 정하고 num개로 나눈 배열 생성
arr_obj = numpy.linspace(start, stop[, num])
    ex) numpy.linspace(0, numpy.pi, 20)
        0 ~ 3.14를 20으로 나누어 배열로 만든다.

특별한 형태의 배열 생성
arr_zeros_n = numpy.zeros(x)
    배열 요소 개수 x개 값 0
arr_zeros_mxn = numpy.zeros((m,n))
    m * n 형태의 2차원 배열 요소 값 0
arr_ones_n = numpy.ones(x)
    배열 요소 개수 x개 값 1
arr_ones_mxn = numpy.ones((m,n))
    m * n 형태의 2차원 배열 요소 값 1
arr_I = numpy.eye(n)
    n * n 형태의 단위행렬

배열의 데이터 타입 변환
num_arr = str_arr.astype(dtype)
    str_arr : 정의된 배열을 .astype()으로 데이터 타입을 변환시킨다.
    dtype :
        float   : 실수
        str     : string
        int     : 정수
num_arr.dtype
    .dtype : num_arr의 데이터 타입 확인

    NumPy 데이터의 형식
        b   bool
        i   기호가 있는 정수, (signed)Integer  : 32비트인지, 64비트인지 구별
        u   기호가 없는 정수, unsigned Integer :
        f   실수, floating-point
        c   복소수, complex-floating point
        M   날짜, datetime
        O   파이썬 객체, (Python)objects
        S or a 바이트 문자열, (byte) string
        U   유니코드, Unicode

난수 배열의 생성
rand_num = numpy.random.rand([d0, d1, ..., dn])
rand_num = numpy.random.randint([low, ] high[, size])
    ex) rand_num = numpy.random.rand(2,3)
        2 * 3의 배열을 랜덤변수로 채운다.
    ex) rand_num = numpy.random.random(1,30,size=(3,4))
        3 * 4의 배열을 1~30사이의 변수들로 채운다.

배열의 계산
일반 정수처럼 '+', '-', '*', '/', '**' 모두 가능하다.

통계를 위한 연산
num_arr = numpy.arange(5)
num_arr.sum()   : 합계
num_arr.mean()  : 평균
num_arr.max()   : 최댓값
num_arr.min()   : 최솟값
num_arr.std()   : 표준편차
num_arr.var()   : 분산
num_arr.cumsum() : 누적합 : 배열형태로 나타난다.
    ex) [1,2,3,4] >> [1,3,6,10]
num_arr.cumprod() : 누적곱 : 배열형태로 나타난다.
    ex) [1,2,3,4] >> [1,2,6,24]

행렬 연산
A = numpy.array([0,1,2,3])
B = numpy.array([3,2,0,1])
    행렬 곲   : A.dot(B), numpy.dot(A,B)
    전치 행렬 : A.transpose(), numpy.transpose(A)
    역행렬    : numpy.linalg.inv(A)
    행렬식    : numpy.linalg.det(A)

배열의 인덱싱과 슬라이싱
num_arr = numpy.arange(10,100,10).reshape(3,3)
    num_arr = [[10,20,30],
               [40,50,60],
               [70,80,90]]
    num_arr[n,m]
        n : 행을 선택
        m : 열을 선택
    num_arr[[n1,n2],[m2,m2]]
        n1, n2 : 행을 선택
        m1, m2 : 열을 선택
        >> [n1, m1], [n2, m2]
    ex) num_arr[[0,2],[0,1]]
        : (0,0), (2,1)을 출력한다. : 10, 80

num_arr[] : 배열에서 요소를 선택
    num_arr[a>3] : 요소를 선택하는 과정에서 조건을 사용할 수 있다.
    ex) num_arr[(a%2)==0]

배열의 슬라이싱
1차원 배열 
    num_arr[시작_위치:끝_위치]
2차원 배열
    num_arr[행_시작_위치:행_끝_위치, 열_시작_위치:열_끝_위치]


"""