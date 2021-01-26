# 에라토스테네스의 체(소수 만들기)
# 이해 안됬음
a = []
for i in range(1, 101):
    a.append(0)
"""
for i in range(1,10,1):
    if(a[i] == 0):
        for j in range(i*2, 101, i):
            a[j] = 1
for i in range(2,101,1):
    if(a[i] == 0):
        print(i, end=" ")
"""
b = []

for i in range(1,22):
    b.append(0)
for i in range(2, 21):
    if(b[i] == 0):
        for j in range(i*2, 21, i):
            b[j] = 1
for i in range(2,101,1):
    if(b[i] == 0):
        print(i, end=" ")