# 1부터 10까지 출력하기
i = 1
while i < 11:
    if i == 10:
        print(i, end="")
    else:
        print(i, end=",")
    i += 1

print()

for i in range(1,11,1):
    if i == 10:
        print(i, end="")
    else:
        print(i, end=",")

print()

# 10부터 1까지 출력하기
i = 10
while i >= 1:
    if (i == 1):
        print(i, end="")
    else:
        print(i, end=",")
    i = i -1

print()

for i in range(10,0,-1):
    if(i == 1):
        print(i, end="")
    else:
        print(i, end=",")

print()

# 1부터 100까지의 합 구하기
sum = 0
for i in range(1, 100):
    sum = sum + i
print(sum)