# 10진수를 2진수로 변환하여 배열에 저장하기
n = int(input("n : "))
b = []
while n != 0:
    b.append(n % 2) # 끝자락에 값을 추가해주는거니까 거꾸로 출력해줘야 2진수가 만들어진다.
    n = n // 2      # '//' : 몫
for i in range(len(b) - 1, -1, -1):
    print(b[i], end=" ")
print()