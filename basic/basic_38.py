# 재귀함수 이용해서 피보나치 수열 구하기

def fibo(a):
    if(a<=2):
        r = 1
    else:
        r = fibo(a-1) + fibo(a-2)
    return r

n = int(input("n : "))
result = fibo(n)
print(result)

# 여기서도 재귀함수 호출하는데 a=1부터 시작해서 호출한다.
# 생각해보면 피보나치함수를 구하기 위해서는 a=1 부터 시작해서 n항을 구하는거기때문에
# 1부터 시작하는게 맞기는한데... basic_37을 보면 함수가 실행되는 과정이
# 직접적으로 받아들여지지는 않음