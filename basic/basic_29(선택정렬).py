# 선택정렬
a = [15, 11, 1, 3, 8]
print(len(a))
for i in range(0, len(a)-1):
    min = i
    for j in range(i+1, len(a)):
        if a[j] < a[min]:
            min = j
    temp = a[i]
    a[i] = a[min]
    a[min] = temp

print(a)

# 선택정렬:
# sort()함수 써버리면 됨 : 정렬시켜주는 함수