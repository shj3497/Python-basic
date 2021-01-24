# break : 명령문을 사용하여 반복문에서 빠져나온다.
# continue : 반복문의 처음으로 돌아가서 다음 반복을 진행한다.
numbers = [1,2,3,4,5]
square = [i**2 for i in numbers]
print(square)

# end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
# while문
print("while문")
count = 1
while count <= 5:
    print("*", end="")
    count += 1
print()

# for문
print("for문")
for i in range(1, 11, 1):
    print("*", end="")

# 중첩 반복
for i in range(1, 3, 1): # 1<= i <3
    for j in range(1, 4, 1): # 1<= i < 4
        print(i, j)
