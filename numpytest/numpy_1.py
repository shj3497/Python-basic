"""
Numpy(Numerical Python)
다차원 배열을 기반으로 수치계산을 빠르게 계산한다.
머신러닝, 딥러닝, 판다스 ... 모듈의 수치계산을 numpy로 한다.

넘파이
1. numpytest : 파이참에서 코드 실행
2. numpy_jupyter : 주피터노트북에서 코드 실행
"""

# 시퀀스 데이터로부터 배열 생성
import numpy

# arr_obj = numpy.array(seq_data)
from numpy.core._multiarray_umath import ndarray

data1 = [0,1,2,3,4,5]
a1 = numpy.array(data1)
print(a1)
print(a1.dtype)

print()
# 요소중 실수가 있다면 자동으로 실수형으로 바뀌네
data2 = [0.1, 5, 4, 12, 0.5]
a2 = numpy.array(data2)
print(a2)
print(a2.dtype)

print()
numpy.array([0.5, 2, 0.01, 8])
print(numpy.array([0.5, 2, 0.01, 8]))

print("2차원 배열")
data3 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(data3)
print(data3.dtype)
print()

# 범위를 지정해 배열 생성
data4 = numpy.arange(0,10,2)
print("data4 : ",data4)

data5 = numpy.arange(0,10,1)
print("data5 : ", data5)

data6 = numpy.arange(5)
print("data6 : ", data6)
print()
## 범위를 지정해서 2차원 배열 생성
# .reshape(행, 열)로 생성한다.
data7 = numpy.arange(12).reshape(4,3)
# 0~11까지의 숫자
# .reshape(행, 열) 로 지정하여 2차원 배열을 만든다.
print("data7 : \n",data7)

print()
data8 = numpy.arange(12).reshape(4,3)
data8_1 = data8.shape # 배열의 형태를 알기위해서 .shape 함수를 실행한다.
print("data8_1 : ", data8_1)

print()
data9: ndarray = numpy.arange(5)
data9_1 = data9.shape
print(data9_1)

# arr_obj = numpy.linspace(start, stop[, num])
# linspace() : start부터 stop까지 num개의 Numpy배열을 생성한다.
data10 = numpy.linspace(1,10,10)
print(data10)

print()
data11 = numpy.linspace(0, numpy.pi, 20)
print(data11)

arr_I = numpy.eye(3)
print(arr_I)

# 배열의 데이터 타입 변환
str_a1 = numpy.array(['1.5','0.62','2','3.14','3.141592'])
print(str_a1)
num_a1 = str_a1.astype(float)
print(num_a1)
bb_a2 = numpy.array(['심혁진', 2, numpy.pi]) # 하나라도 스트링이 있으면 배열 타입은 스트링으로 변환
print(bb_a2)
print()
num_a2 = numpy.arange(10)
print(num_a2)
print(num_a2.dtype)
str_a2 = num_a2.astype(str)
print(str_a2)
print(str_a2.dtype)

# 난수 배열의 생성
data12 = numpy.random.rand(2,3) # 2*3형태의 배열 랜덤변수로 채움
print("data12" , data12)
data13 = numpy.random.rand() # 랜덤변수 하나 출력
print("data13", data13)
data14 = numpy.random.rand(2,3,4) # 2*(3*4) 라는 3차원 배열 생성?
print("data14 : ", data14)

data15 = numpy.random.randint(10, size=(3,4)) # 3*4 배열, 10이하의 숫자들로
print("data15 \n", data15)
data16 = numpy.random.randint(1,30) # 1부터 30까지의 숫자, size 지정 x 변수 출력
print("data16 \n", data16)
print()

# 배열의 계산
arr1 = numpy.array([10,20,30,40])
arr2 = numpy.array([1,2,3,4])
data17 = arr1 + arr2
print(data17)
data18 = arr1 - arr2
print(data18)
data19 = arr2 *2
print(data19)
data20 = arr2**2
print(data20)
data21 = arr1 * arr2
print("data21 \n", data21)
data22 = arr1 / arr2
print(data22)
data23 = arr1 / (arr2**2)
print("data23\n", data23)
data24 = arr1 > 20
print("data24\n", data24)
print()

# 통계를 위한 연산
arr3 = numpy.arange(5)
print("arr3 : ", arr3)
arr3_sum = arr3.sum() # 합계
arr3_mean = arr3.mean() # 평균
print("arr3_sum : ", arr3_sum, " arr3_mean : ", arr3_mean)
arr3_std = arr3.std() # 표준편차
arr3_var = arr3.var() # 분산
print("arr3_std : ",arr3_std, " arr3_var : ",arr3_var)
arr3_min = arr3.min() # 최솟값
arr3_max = arr3.max() # 최댓값
print("arr3_min : ",arr3_min, " arr3_max : ",arr3_max)

arr4 = numpy.arange(1,5)
print("arr4 : ", arr4)
arr4_cumsum = arr4.cumsum() # 누적합을 배열로 나타낸다.
print("arr4_cumsum : ", arr4_cumsum)
arr4_cumprod = arr4.cumprod() # 누적곱을 배열로 나타낸다.
print("arr4_cumprod : ", arr4_cumprod)

# 행렬 연산
A = numpy.array([0,1,2,3]).reshape(2,2)
print("A \n", A)
B = numpy.array([3,2,0,1]).reshape(2,2)
print("B \n", B)

C = A.dot(B)
print("C \n", C)
C_1 = numpy.dot(A,B) # 행렬 곲
print(C_1)
A_T = numpy.transpose(A) # 전치행렬
print("A의 전치행렬 : \n", A_T)
A_l = numpy.linalg.inv(A) # 역행렬
print("A의 역행렬 : \n", A_l)
A_d = numpy.linalg.det(A) # 행렬식 (ad-bc)
print("A의 행렬식(ad-bc) : \n", A_d)
print()

# 배열의 인덱싱과 슬라이싱
a1 = numpy.array([0,10,20,30,40,50])
print(a1)
a1[5] = 70
print(a1)
print(a1[[1,3,4]]) # 여러개 호출할때는 [[]] 대괄호가 두개네..
# 호출할 때도 배열로 호출한다는 소리
print()
a2 = numpy.arange(10,100,10).reshape(3,3)
print(a2)
print(a2[0,2])
a2[2,2] = 95
print(a2[2,2])
print(a2[1]) # 오호.. 2차원 배열에서는 행이 출력 되는군
a2[1] = numpy.array([45,55,65]) # 2차원 배열에서 행을 삽입해서 바꿔준다.
print(a2)
a2[1] = numpy.array([47,57,67])
print(a2)
print(a2[[0,2],[0,1]]) # 0,0 좌표랑, 2,1좌표를 가지고 왔다.
print()
a = numpy.array([1,2,3,4,5,6])
print(a[a>3]) # 요소를 선택하는 과정에 있어 조건을 사용할 수 있다.
print(a[(a%2)==0])
print()

# 배열의 슬라이싱
b1 = numpy.array([0,10,20,30,40,50])
print(b1[1:4])
print(b1[:3])
print(b1[2:])
b1[2:5] = numpy.array([25,35,45])
print(b1)
b1[3:6] = 60
print(b1)
print()

b2 = numpy.arange(10,100,10).reshape(3,3)
print(b2)
print(b2[1:3, 1:3])
print(b2[:3, 1:]) # 0,1,  0,2,  1,1,  1,2,  2,1,  2,2
print(b2[1][0:2])
# ==
print(b2[1, 0:2])
b2[0:2, 1:3] = numpy.array([[25,35],[55,65]])
print(b2)