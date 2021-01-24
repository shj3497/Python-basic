# 나이에 따른 입장료

charge = 5000
age = int(input("나이를 입력하세요 >>> : "))
if age < 8:
    charge = 0
elif age < 60:
    charge = charge
else:
    charge = charge / 2

print("요금 >>> : ", str(charge))

print(f"요금 : {charge * 0.5} 입니다.")

print()

# 3의 배수이면서 5의 배수 판별하기

a = int(input("숫자를 입력하세요 >>> : "))
if a % 3 == 0 and a % 5 == 0:
    print("3의 배수이면서 5의 배수입니다.")
else:
    print("3의 배수이면서 5의 배수가 아닙니다.")

print()

b = int(input("숫자를 입력하세요 >>> : "))
if b % 3 == 0:
    if b % 5 == 0:
        print("3의 배수이면서 5의 배수입니다.")
    else:
        print("3의 배수이지만 5의 배수는 아닙니다.")
else:
    print("3의배수가 아닙니다.")
