# 배열에 저장된 2진수를 10진수로 변환하기
b = [1,1,0,0,1] # 25
n = 0
for i in range(0, 5):
    n = n +( b[i] * (2 ** (4-i)) )
    # 괄호 주의해서 사용
    print(n)

print(n)

# 선형탐색
def linear_search(element, some_list):
    for i in range(len(some_list)):
        if (element == some_list[i]):
            return i
    return None

print("선형 탐색")
print(linear_search(2, [2,3,6,5,11,23,34,66]))
print(linear_search(11, [2,3,6,5,11,23,34,66]))
print(linear_search(34, [2,3,6,5,11,23,34,66]))
print(linear_search(66, [2,3,6,5,11,23,34,66]))
print(linear_search(25, [2,3,6,5,11,23,34,66]))