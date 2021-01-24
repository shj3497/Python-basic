# 최댓값 구하기
a = int(input("a >> : "))
max = 0
while a != 0:
    print("종료시 0을 입력하세요")
    if(a > max):
        max = a
    a = int(input("a >>> : "))
print("max >>> : ", max)

# 직각삼각형 모양으로 수 출력하기
for i in range(2,7,1):
    for j in range(1,i,1):
        print(j, end=" ")
    print()