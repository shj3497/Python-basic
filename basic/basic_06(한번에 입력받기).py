# 사각형 넓이 구하기
import math

a = int(input("가로길이를 입력하세요 >>> : "))
b = int(input("세로길이를 입력하세요 >>> : "))
print("사각형 넓이 >>> : ", a * b)

# 한번에 입력받기
d, e, f = input("입력 :").split(',')
print(d, e, f)
a, b = map(int, input("숫자 두개를 입력하세요").split(','))
print(a, b)

print()

# 원 넓이 구하기
r = int(input("반지름을 입력하세요 >>> : "))
print("원의 넓이 >>> : ", r * r * math.pi)

print()

# 총점과 평균 구하기
a = int(input("a를 입력하세요 >>> : "))
b = int(input("b를 입력하세요 >>> : "))
c = int(input("c를 입력하세요 >>> : "))
sum = a + b + c
print("합계 >>> : ", sum, "평균 >>> : ", sum / 3)