# 버블정렬
# 값이 큰것을 오른쪽에 밀어서 정렬시킴
a = [15, 11, 1, 3, 8]
for i in range(0, len(a)-1):
    for j in range(0, (len(a)-1)-i, 1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print(a)