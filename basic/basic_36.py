# 함수를 이용해서 1부터 10까지의 약수 구하기
def func(a):
    for i in range(1, a+1, 1):
        if(a % i == 0):
            print(i, end=" ")

for i in range(1, 11, 1):
    print(i, end="의 약수 : ")
    func(i)
    print()
