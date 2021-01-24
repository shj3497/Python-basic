# 최대 공약수 구하기
n1 = int(input("n1 >>> : "))
n2 = int(input("n2 >>> : "))
for i in range(n1, 1, -1):
    if(n1 % i == 0 and n2 % i == 0):
        print("i >>> : ", i)
        break
print()

# 소수 판별하기
chk = 1
n = int(input("n : "))
for i in range(2, n, 1):
    if(n % i == 0):
        chk = 0
if(chk == 1):
    print("소수")
else:
    print("소수가 아님")

print()

# 피보나치 수열 구하기
a, b = 1, 1
print(a, b, end=" ")
for i in range(3, 20, 1):
    c = a+b
    print(c, end=" ")
    a = b
    b = c
