# 1, (1+2), (1+2+3), ... (1+2+...+10)의 합 구하기
for i in range(2,12,1):
    sum = 0
    for j in range(0, i, 1):
        sum = sum + j
    print(sum)

# 구구단
for i in range(2,10,1):
    for j in range(2, 10, 1):
        print("(",i,"*",j,")", "=", i*j, end=" ")
    print()