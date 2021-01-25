# 1부터 10까지의 수 저장하고 출력하기
lang = []
for i in range(1,11,1):
    lang.append(i)
print(lang)

print()

# 10,20,30 ... , 100 저장하고 거꾸로 출력하기
print("10,20,30 ... , 100 저장하고 거꾸로 출력하기")
lang1 = []
for i in range(1, 11, 1):
    lang1.append(i*10)
for j in range(9, -1, -1):
    print(lang1[j], end=" ")

print()
print()
# 배열 요소 거꾸로 뒤집기
print("배열 요소 거꾸로 뒤집기")
# temp = [0 for i in range(10)] >> : 길이를 10으로 하고 값들을 0으로 초기화
a = []
temp = []
for i in range(1, 11):
    a.append(i)
    temp.append(a[i-1])
for i in range(1, 11):
    a[10-i] = temp[i-1]
print(temp)
print(a)
# 흠.. 출력은 됬는데 뭔가 찝찝함