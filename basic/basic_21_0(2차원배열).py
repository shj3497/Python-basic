# 2차원 배열 선언시 컴프리핸션 사용할 것!!
# 단순 배열 곱으로는 2차원이 만들어지지 않는다.
# ex)
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

array[0][1] = 4
print(array)
# basic_21_1 참조할 것