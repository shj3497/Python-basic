# 세 수중 가장 큰 수 찾기
# 방법 1
a = int(input("a >>> : "))
b = int(input("b >>> : "))
c = int(input("c >>> : "))

if a > b:
    if a > c:
        print("가장 큰 수 a >>> : ", a)
    else:
        print("가장 큰 수 c >>> : ", c)
else:
    if b > c:
        print("가장 큰 수 b >>> : ", b)
    else:
        print("가장 큰 수 c >>> : ", c)

# 방법 2
max = int(input("max >>> : "))
a = int(input("a1 >>> : "))
if a > max:
    max = a
a = int(input("a2 >>> : "))
if a > max:
    max = a
print("max >>> : ", max)
