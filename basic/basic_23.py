# 배열 a요소 배열 b에 거꾸로 저장하기
a = [i for i in range(1,11)]
print(a)
b = []
for j in range(9, -1, -1):
    b.append(a[j])
print(b)


# 배열 요소 왼쪽으로 한칸씩 원형으로 이동하기
a=[]
for i in range(1,11):
    a.append(i)
print(a)
temp = a[0]
for i in range(1,9):
    a[i] = a[i+1]
