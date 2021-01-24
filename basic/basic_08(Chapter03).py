# 두 수중 큰 수 찾기
a = int(input("a >>> : "))
b = int(input("b >>> : "))

if a > b:
    print("a > b", a)
else:
    print("a < b", b)

# 양수, 0, 음수 판별하기
a = int(input("a >>> : "))
if a > 0:
    print("양수")
elif a < 0:
    print("음수")
else:
    print("0")
