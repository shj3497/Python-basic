# 병합정렬
# 각 리스트의 숫자를 비교하여 새로운 리스트에 집어 넣음
a = [1, 3, 5, 7]
b = [4, 3, 6, 10]
c = []
i = 0
j = 0
k = 0
while i<len(a) and j<len(b):
    a.sort()
    b.sort()
    if a[i] < b[j]:
        c.append(a[i])
        i = i+1
    else:
        c.append(b[j])
        j = j+1

if i == len(a):
    while j < len(b):
        c.append(b[j])
        j = j+1
    else:
        print(c)
else:
    while i < len(a):
        c.append(a[i])
        i = i+1
    else:
        print(c)

############################################
# 정렬되어있지않는 배열 a를 가지고 반으로 쪼개서 병합정렬을 하는 과정
# a는 배열
def merge_sort(a):
    n = len(a)

    # 종료 조건 : 정렬한 리스트의 자료 개수가 한개 이하이면  정렬할 필요가 없다.
    if n <= 1:
        return

    # 그룹을 나누어 각각 병합 정렬을 호출하는과정
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)

    # 두 그룹을 합치는 과정(병합)
    i1 = 0
    i2 = 0
    ia = 0

    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 = i1 + 1
            ia = ia + 1
        else:
            a[ia] = g2[i2]
            i2 = i2 + 1
            ia = ia + 1
    if i1 == len(g1):
        while i2 < len(g2):
            a[ia] = g2[i2]
            i2 = i2 + 1
            ia = ia + 1
    else:
        while i1 < len(g1):
            a[ia] = g1[i1]
            i1 = i1 + 1
            ia = ia + 1

d = [3, 1, 5, 7, 4, 3, 6, 10]
print(d)
merge_sort(d)
print(d)

