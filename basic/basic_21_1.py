# 리스트 연습
data = [1,2,3,4,5]
print(data)
print(type(data))
print(data[0])
print(data[1:3])
print(len(data))
print(data[-1])
print(data[-3])
data[3] = 7
print(data)

data = list()
print(data)
data = []
print(data)

# 초기화
n=10
a=[0] * n
print(a)
b=[0 for i in range(10)]
print(b)

# 리스트 컴프리헨션 : list comprehension
# 홀수
array = [i for i in range(20) if(i % 2 == 1)]
print(array)

# 언더바 : _
# 반복을 수행하되 반복을 위한 변수의 값을 무시하고 할 때는 언더바(_)를 사용한다.
for _ in range(5):
    print("hello Python")

# n*m 크기의 2차원 리스트 초기화
print("n*m 크기의 2차원 리스트 초기화")
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

n1 = 3
m1 = 4
array1 = [[0] * m1] * n1
print(array1)

print()

array[0][1] = 5
array1[0][1] = 5
print(array)
print(array1)

print()

array[1][0] = 5
array1[1][0] = 5
print(array)
print(array1)
# 정리 : 2차원 배열을 만들때는 컴프리핸션을 이용해서 만들어야한다.
# 그렇지 않으면 배열요소에 값을 넣을때 엉망으로 들어감
print()

a = list([1,4,3])
a1 = [1,4,3]

print("기본리스트 >>> : ", a)
print("기본리스트 >>> : ", a1)

a.append(2)
print("삽입 >>> : ", a)

a.sort()
print("오름차순 정렬 >>> : ", a)

a.sort(reverse=True)
print("내림차순정렬 >>> : ", a)

a.reverse()
print("배열 뒤집기 >>> : ", a)

a.insert(2, 3)
print("배열 2번째 자리에 5을 추가한다.", a)

b = a.count(3)
print("값이 3인 데이터 개수 >>> : ", b)

a.append(3)
a.remove(3)
print("입력값과 첫 번째로 일치하는 항목을 리스트에서 제거 >>> : ", a)

print()

# remove
zz = [1,2,3,4,5,5,5]
remove_set = {3,5}
result = [i for i in zz if i not in remove_set]
print(result)