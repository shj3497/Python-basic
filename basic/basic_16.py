# 계승 구하기
fact = 1
for i in range(5, 1, -1):
    fact = fact * i
    print("fact >>> : ", fact)
print("fact >>> : ", fact)

print()

# 약수 구하기
n = int(input("n을 입력하세요 : "))
for i in range(1, n+1, 1):
    if(n % i == 0):
        print(i, end=" ")

print()

# 공약수 구하기
n1 = int(input("n1을 입력하세요 : "))
n2 = int(input("n2을 입력하세요 : "))

for i in range(1, n2+1, 1):
    if(n1 % i == 0 and n2 % i == 0):
        print(i, end=" ")
