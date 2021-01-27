myFriends = ['James','Robert','Lisa','Mary']
for myFriend in myFriends:
    print(myFriend)

print(range(0,10,1))
print(list(range(0,10,1)))
names = ['James','Robert','Lisa','Mary']
scores = [95, 96, 97, 94]

for k in range(len(names)):
    print(names[k], scores[k], end=" ")
print()
# zip() : 같은 길이의 데이터를 하나의 하나로 묶어주는 zip() 이있다.
for name, score in zip(names, scores):
    print(name, score, end=" ")
print()
# while
i = 0
sum = 0
while sum<20:
    i = i+1
    sum = sum + i
    print(i, sum)
print()
# break
k = 0
while True:
    k = k+1
    if k>3:
        break
    print(k)
print()
for k in range(10):
    if(k>2):
        break
    print(k)
print()
# continue : 를 만나면 반복문의 처음으로 돌아가서 다음 반복을 진행한다.(건너뛰라는 의미)
for k in range(5):
    if k==2:
        continue
    print(k)
print()
k=0
while True:
    k = k + 1
    if k==2:
        print("continue next")
        continue
    if k>4:
        break
    print(k)
print()
# 간단하게 반복하는 한줄 for문
numbers = [1,2,3,4,5]
square = []
for i in numbers:
    square.append(i**2)
print(square)
print()

numbers = [1,2,3,4,5]
square = [i**2 for i in numbers]
print(square)
print()

numbers = [1,2,3,4,5]
square = []
for i in numbers:
    if i>=3:
        square.append(i**2)
print(square)