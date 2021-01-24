import sys
# 문자열 : readLine(), readLines()
a = int(input("a : "))

a = sys.stdin.readline().rstrip()

a = int(a)
print(type(a))

i = 10
print("i = ", str(i)) # 문자로 형변환해서 출력
print(f"i = {i} 입니다.")
