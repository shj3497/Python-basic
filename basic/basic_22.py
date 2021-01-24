# 1부터 10까지의 수 저장하고 출력하기
lang = []
for i in range(1,11,1):
    lang.append(i)
print(lang)

print()

# 10,20,30 ... , 100 저장하고 거꾸로 출력하기
lang1 = []
for i in range(1, 11, 1):
    lang1.append(i*10)
for j in range(9, -1, -1):
    print(lang1[j], end=" ")

print()

# 배열 요소 거꾸로 뒤집기


