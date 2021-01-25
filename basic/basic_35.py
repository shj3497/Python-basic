# 함수 이용해서 세 수 중 큰 수 찾기

def func(a,b,c):
    if(a > b):
        if(a > c):
            m = a
        else:
            m = c
    else:
        if(b > c):
            m = b
        else:
            m = c
    return m

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

r = func(a,b,c)
print(r)


