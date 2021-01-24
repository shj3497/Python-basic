import keyword
# print(keyword.kwlist)
kwlist = keyword.kwlist
print(kwlist)


# "[{:10}]"은 [] 괄호안의 글자를 0~9로 제한한다는 뜻
for i in range(0, len(kwlist)):
    print("[{:10}]".format(kwlist[i]), end="") 
    if (i+1) % 5 == 0:
        print()

# for문을 쓸때 자바와는 다르게 for i in range(범위)로 설정해준다.
# : 기호는 함수를 시작한다는 {} 중괄호 역할을 하며,

print(11/3)
print(11%3)
print(11//3)
print(11**3)

def draw_stars(y):
    return '*' * y

print(draw_stars(3))

