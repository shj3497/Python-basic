# 1부터 100까지의 수 중 짝수의 합 구하기
sum = 0
for i in range(2, 101, 2):
    sum = sum + i
print("sum >> : ", sum)

# 1, -2, 3, -4, ... -100의 합 구하기
sum = 0
for i in range(1, 100, 1):
    if(i % 2 == 0):
        sum = sum - i
    if(i % 2 == 1):
        sum = sum + i
print("sum >>> : ", sum)