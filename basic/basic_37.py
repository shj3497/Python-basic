# 재귀함수 이용해서 1부터 입력받은 수까지의 합 구하기
def sum(a):
    if(a > 1):
        r = a + sum(a-1)
    else:
        r = 1
    print("a >>> : ", a)
    print("r >>> : ", r)
    return r

# 입력받은 a값 부터가 아닌 1부터 증가하여 계산을 한다.
# 왜일까?
# 일반적인 생각으로라면 sum(10): r = 10 + sum(9) = 10 + 9 + sum(8) ...
# sum(10): r = 10 + ...+ 2 + sum(1): r = 1 이 되어
# r = 10 + ... + 1이 되어야 할텐데..


n = int(input("n : "))
result = sum(n)
print(result)
