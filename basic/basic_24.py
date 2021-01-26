# 배열 최댓값 구하기
import random

a = []
for i in range(1,11):
    a.append(random.randint(1,100))
print(a)
m = a[0]
for i in range(1, len(a)):
    if(m < a[i]):
        m = a[i]
print("최댓값 : ", m)

min = min([2,1,4,6,4])
print("min : ", min)
max = max([1,4,6,8,2])
print("max : ", max)

b = [5,3,8,1,2,8,2,4,7,12]
max(b)
