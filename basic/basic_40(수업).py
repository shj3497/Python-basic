def calcrange(begin, end):
    sum = 0
    for num in range(begin, end+1):
        sum += num
    return sum
print("3 ~ 7 = ", calcrange(3, 7))

def printsum(n):
    sum = 0
    for num in range(n+1):
        sum += num
    return print("~", n, "=", sum)

printsum(4)
printsum(10)

# *args : tuple : 튜플로
# *ints의 의미 : '*'가 배열을 받는다는 것
def intsum(*ints):
    sum = 0
    for num in ints:
        sum += num
    return sum

print("intsum", intsum(1,2,3))
print("intsum", intsum(5,7,9,11,13))
print("intsum", intsum(8,9,6,2,9,7,5,8))

# **의 의미 : '**'가 dictionary의 key값을 가진다는 의미인듯
def save_ranking(**kwargs):
    print(kwargs)
save_ranking(first="ming", second='alice', fourth='wilson', third='tom', fifth='roy')

# ==========calcstep============
def calcstep(begin, end, step=1):
    sum = 0
    for num in range(begin, end+1, step):
        sum += num
    return sum

print("1~10 = ", calcstep(1,10,2))
print("1~10 = ", calcstep(1,10))

# keyword var arg : dictionary : 사전
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(a=1, b=3)
print()
# key값으로 변수를 받았으니 두개의 print()가 일치하게 나옴
def calcstep(**args):
    begin = args['begin']
    end = args['end']
    step = args['step']
    sum = 0
    for num in range(begin, end+1, step):
        sum += num
    return sum
print('3~5 = ', calcstep(begin=3, end=5, step=1))
print('3~5 = ', calcstep(step=1, end=5, begin=3))
print()

def calcscore(name, *score, **option):
    print(name)
    sum =0
    for s in score:
        sum +=s
    print("총점 : ", sum)
    if option['avg'] == True:
        print("평균 : ", sum/len(score))
calcscore("안석현", 88,99,77, avg=True)
calcscore("심혁진", 88,99,77, avg=False)
print()

# 람다 : lamdba : 익명함수 : 이름이 없는 함수
# 자바에서는 람다를 별로 안좋아한다 : 재사용이 힘들다
# 파이썬, Vue : 람다를 선호
print("람다 : lambda")
def a(x):
    return x+10
print("함수 ::: a(1) >>> : ", a(1))
print()

# 람다 표현식 함수
b = lambda x: x+10
print("lambda ::: b(1) >>> : ", b(1))
print()

# 표현식 자체 호출 : 람다식에 괄호를 만들어줬다?(1)이라는 변수도 대입해줬고?
a = (lambda x : x+10)(1)
print("lambda ::: a >>> : " , a)
print()

# 람다 표현식 안에서는 변수를 만들수 없다.
# a = (lambda x : y=10; x+y)(1)
y=10
c = (lambda x: x+y)(1)
print("lambda ::: c >>> : ", c)
print()

# 그러니까 함수명 = (lambda 변수이름선언 : 함수식)(변수 선언)으로 람다식을 만드는거네
d = (lambda t, v : t+v)(2, 10)
print("lambda ::: d >>> : ", d)
print()

# 람다 표현식을 인수로 사용
a = list(map(lambda x : x + 10, [1,2,3]))
print("lambda ::: a >>> : ", a)
print()

# 튜플 자료형
# 튜플은 한번 선언된 값을 변경할 수 없다.
# 순차적으로 저장
# 리스트는 대괄호를 이용하지만 튜플은 소괄호를 이용한다.
a= (1,2,3,4)
print(a)
print(type(a))
print()

# 딕셔너리 : 사전 자료형(해시맵)
# 딕셔너리 : 순차가 없다.
# 리스트, 튜플 : 순차가 있다.
data = dict()
data['사과']='Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)
print()

if '사과' in data:
    print("'사과'를 키로가지는 데이터가 존재")

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)
print()

for key in data.keys():
    print(key, end=" ")
print()
for value in data.values():
    print(value, end=" ")
print()

# 집합 자료형 set
# 중복 허용x
# 순서가 없다.
data = set([1,1,2,3,4,4,5])
print(data)
print(type(data))
print()
data = {1,1,2,3,4,4,5}
print(type(data))
print("list : []", "tuple : ()", "set : {}")
print()

a = {1,2,3,4,5}
b = {3,4,5,6,7}

print("합집합 '|' : ", a|b)
print("합집합 '.union()' : ", a.union(b))
print("교집합 '&' : ", a&b)
print("교집합 '.intersection()' : ", a.intersection(b))
print("차집합 '-' : ", a-b)
print("차집합 '.difference()' : ", a.difference(b))
print()

# enumerate 함수
data = enumerate((1,2,3))
print(data, type(data))
for i, value in data:
    print(i, ":", value)
print()

data = enumerate({1,2,3})
print(data, type(data))
for i, value in data:
    print(i, ":", value)
print()

# i는 자동으로 증가하는건가?
data = enumerate([1,2,3])
print(data, type(data))
for i, value in data:
    print(i, ":", value)
print()

# i는 자동증가가 맞는듯
dict1 = {'이름':'심혁진', '나이':21}
data = enumerate(dict1)
for i, key in data:
    print(i, ":", key, dict1[key])
print()

data = enumerate("심혁진 최태양 김종혁")
for i, value in data:
    print(i, ":", value)
print()

#
def kim():
    temp = '김과장의함수'
    print(temp)

def lee():
    temp = 2**10
    print(temp)

def park(a):
    temp = a*2
    print(temp)

kim()
lee()
park(9)

print()
#
salerate = 0.9

def kim():
    print("오늘의 할인율 : ", salerate)

def lee():
    price = 1000
    print("가격 : ", price * salerate)
kim()
salerate = 1.1
lee()
print()

#
price = 1000

def sale():
    price=500

sale()
print(price)

# id() : 파이썬이 객체를 구별하기 위해서 부여하는 일련번호
# 숫자로서의 의미는 없다.
# 메모리에 올라가있는 주소정도의 의미로 이해하면 좋을듯
price = 1
print("price >>> : ", id(i))

#
price = 1000

def sale():
    price =500
    print("sale", id(price))
sale()
print()
