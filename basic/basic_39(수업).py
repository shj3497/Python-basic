# 정수
a = 1000
print(a)

a = -7
print(a)

a = 0
print(a)

# 실수
a = 157.93
print(a)

a = -1837.2
print(a)

a = 5.
print(a)

a = -.7
print(a)

# 지수
# 실수형 데이터를 표현하는 방식 e, E 지수표현 방식을 이용
# e  다음에 오는 수는 10의 지수부 의미
# 1e9 : 10의 9제곱 : 1,000,000,000
a = 1e9
print(a)

a = 75.25e1
print(a)

a = 3954e-3
print(a)

# 부동 소수점 : Floating-point
# IEEE754 표준에서 실수를 저장히기 위해 4바이트, 8바이트 고정 메모리를 할당
# 현대 컴퓨터 시스템은 대체로 실수 정보를 표현하는데 정확도에 한계가 있다.
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

# round(a, 4) 소수점 4째자리에서 반올림
a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)

# 수 자료형 연산
a = 7
b = 3

print(a/b)
print(a%b)
print(a//b)
print(a**3)

# list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(type(a))
print(a[4])
print(a[1:4])
print(a[-1])
print(a[-3])
a[3] = 7
print(a)

a = list()
print(a)
a = []
print(a)

n = 10
a = [0] * n
print(a)

# 리스트 컴프리헨션 : list comprehension
# 홀수
array = [i for i in range(20) if i%2 == 1]
print(array)

array = [i * i for i in range(1, 10)]
print(array)

# 언더바 : _
# 반복을 수행한되 반복을 위한 변수의 값을 무시하고자 할 때는 언더바(_) 사용
for _ in range(5):
    print("Hello World")

# n * m 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)


array[1][1] = 5
print(array)

# 특정한 크기의 리스트를 초기화 할 때는 리스트 컴프리헨션을 사용해야 한다.
n = 3
m = 4
array = [[0] * m] * n
print(array)


array[1][1] = 5
print(array)


# 리스트 함수
a = ([1, 4, 3])
print("기본 리스트 >>> : ", a)

a.append(2)
print("삽입 >>> : ", a)

a.sort()
print("오름차순 정렬 >>> : ", a)

a.sort(reverse=True)
print("내림차순 정렬 >>> : ", a)

a.reverse()
print("원소 뒤집기 >>> : ", a)

a.insert(2,3)
print("인덱스 2에 3추가 >>> : ", a)

a1 = a.count(3)
print("값이 3인 데이터 갯수 >>> : ", a1)

a.remove(1)
print("특정 값 데이터 삭제 >>> : ", a)

# remove
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)


# 문자열 "" '' """""" ''''''
# 이스케이프 문자  백슬래시(\) 사용 큰따옴표 나 작은 따옴표 사용
data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

# 듀플 자료형
# 듀플은 한 번 선언된 값을 변경할 수 없다.
# 순차적으로 저장
# 리스트는 대괄호([])를 이용하지만, 듀플은 소괄호(())를 이용한다.

a = (1, 2, 3, 4)
print(a)

# tuple object dose not support item assignment
# a[2] = 7

# 딕셔너리 : 사전 자료형
# 사전 자료형은 key : value
# 딕션너리 : 순차가 순차가 없다.
# 리스트, 듀플 : 순차가 있다.

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'


print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재한다. ")


key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)


for key in key_list:
    print(data[key])


# 집합 자료형 :set
# 중복을 허용하지 않는다.
# 순서가 없다.

data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5}

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b)
print(a & b)
print(a - b)

data = set([1, 2, 3])
print(data)

data.add(4)
print(data)

data.update([5, 6])
print(data)

data.remove(3)
print(data)