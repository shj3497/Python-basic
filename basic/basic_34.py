# 함수 이용해서 두 수중 큰 수 찾기
a = int(input("a >> : "))
b = int(input("b >> : "))

def func(a,b):
    if(a > b):
        m = a
        print("a > b")
    elif(a < b):
        m = b
        print("a < b")
    else:
        print("a = b")
    return m
r = func(a,b)
print(r)
