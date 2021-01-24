# 1부터 10까지의 정수에 대한 약수 구하기
for i in range(2, 11, 1):
    print(i, "의 약수 : ", end="")
    for j in range(1, i+1, 1):
        if(i % j == 0):
            print(j, end=" ")
    print()

print()

# 2부터 100까지의 소수 구하기
for i in range(2, 101, 1):
    chk = 1
    for j in range(2, i, 1):
        if(i % j == 0):
            chk = 0
    if(chk == 1):
        print(f"{i}는 소수입니다.")