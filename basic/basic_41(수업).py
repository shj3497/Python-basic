# index
s = 'python'
print(s[2])
print(s[-2])

# stringindex
s=  'python'
for c in s:
    print(c, end=', ')

# slice
s = 'python'
print(s[2:5])
print(s[3:])
print(s[:4])
print(s[2:-2])

# slice2
file = "20210127-104830.jpg"
print("촬영날짜 : ", file[4:6], "월", file[6:8], "일")
print("촬영시간 : ", file[9:11], '시', file[11:13], '분')
print("확장자 : ", file[-3:])

# slice3
yoil = '월화수목금토일'
print(yoil[::2])
print(yoil[::-1])

# find
s = "python programing"
print(len(s))
print(s.find('o'))  # find()  : 'o'를 왼쪽부터 찾기 시작해서 몇번째 자리에 있는지
print(s.rfind('o')) # rfind() : 'o'를 오른쪽부터 찾기 시작해서 몇번째 자리에 있는지
print(s.index('r')) # index() : 'r'의 첫번째 출현자리
print(s.count('n')) # count() : 'n'의 출현횟수

# count
s = "생각이랑 생각할 수록 생각나므로 생각하지 말아야 할 생각은 생각하지 않으려고 하는 생각이 옳은 생각각이라고 합니다."
print("생각의 출현 횟수 :" , s.count("생각"))

# in : 특정문자가 들어있는지 판단해서 True, False로 반환
s = "python programming"
print('a' in s)
print('z' in s)
print('pro' in s)
print('x' not in s)

# startswith : 문자열의 첫번째 글자 판단
name='심혁진'
if name.startswith("심"):
    print("심")
if name.startswith("혁"):
    print("혁")

# endswith : 문자열의 뒤에서 부터 글자를 세서 판단
file = 'girl.jpg'
if file.endswith('.jpg'):
    print("확장자 : jpg")

# isdecimal() : 문자를 숫자로 형변환 해주는듯? 종류가 많음
'''height = input("키를 입력하세요 : ")
if height.isdecimal():
    print("키 = ", height)
else:
    print("숫자만 입력")
'''
# lower() : 소문자로
# upper() : 대문자로
s = "Good morning. my love KIM."
print(s.lower())
print(s.upper())
print(s)
print(s.swapcase())     # 입력받은 문자열 대소문자 뒤집기
print(s.capitalize())   # 
print(s.title())    # 각 단어의 첫글자를 전부 대문자로 표시

# strlower
"""
python = input("파이썬의 영문 철자를 입력하시오 : ")
if python.lower() == "python":
    print("맞췄습니다.")

"""
# strip() : 공백제거
# lstrip() : 왼쪽 공백제거
# rstrip() : 오른쪽 공백제거
s = "  angel   "
print(s + "님")
print(s.lstrip() + "님")
print(s.rstrip() + "님")
print(s.strip() + "님")

#  split() : 문자열을 공백기준으로 쪼개서 list로 만듬
s = "짜장 짬뽕 탕슉"
print(s.split(), type(s.split()))

# splis("") : ""안에 들어가있는 문자열 or 공백으로 문자열을 쪼개서 list로 만듬
s2 = "서울->대전->대구->부산"
city = s2.split("->")
print(city)
for c in city:
    print(c, "찍고", end = ' ')


# splitlines : 문자열을 한라인씩 쪼개서 리스트로 만든다.
# \n\n이 있는경우 공백이껴있으므로 공백마저 리스트에 포함됨을 알 수 있다.
traveler = """강나루 건너서\n밀밭 길을\n\n구름에 달 가듯이\n가는 나그네\n
길은 외줄기\n남도 삼백리\n\n술 익는 마을마다\n타는 저녁놀\n
구름에 달 가듯이\n가는 나그네"""
poet = traveler.splitlines()
print(poet)
for line in poet:
    print(line)
print()

#  join : 각 문자마다 정의한 문자열 삽입?
s = "._."
print(s.join("대한민국"))

#  splitjoin
s2 = "서울->대전->대구->부산"
city = s2.split("->")
print(city)
print(" 찍고 ".join(city))
print()

#  replace() : 특정 문자를 다른 문자로 바꿈
s = "독도는 일본땅이다. 대마도도 일본땅이다."
print(s)
print(s.replace("일본", "한국"))
print()

#  just() : 문자열을 포함해서 30칸을 만든다.
# ljust(), rjust(), center() 이있다.
message = "안녕하세요."
print(message.zfill(10))
print(message.ljust(30)) # 왼쪽에 문자열 정렬하고 최대 30칸까지 공백으로 체움
print(message.rjust(30)) # 오른쪽에 문자열 정렬하고 최대 30칸까지 공백으로 채움
print(message.center(30)) # 중앙정렬하고 최대 30칸까지 공백으로 채움

# === center ===
traveler = """강나루 건너서\n밀밭 길을\n\n구름에 달 가듯이\n가는 나그네\n
길은 외줄기\n남도 삼백리\n\n술 익는 마을마다\n타는 저녁놀\n
구름에 달 가듯이\n가는 나그네"""
poet = traveler.split() # splitlines와는 다르게 공백은 제거하네..
print(poet)
for line in poet:
    print(line.center(30))

# stringcat
# str() : 숫자를 문자열로 바꿈
# isdecimal() : 문자를 숫자로 바꿈
price = 500
print("궁금하면 ", str(price), '원!')

# format
# 문자열에 %x라는 기호를 넣고 %()로 %x에 넣을 값을 정의해준다.
# key:value가 아니라 %()에 정의해준 값이 순서대로 들어간다.
price = 500
print("궁금하면 %d원!" %(price))

# format2
month = 8
day = 15
anni = "광복절"
print("%d월 %d일은 %s이다." % (month, day, anni))

# width
value = 1231111
print("###%d###" %(value))
# %5d(다섯글자제한) but, 글자수 제한보다 값을 입력하는게 우선
# >> 5글자로 제한했지만 7글자를 입력하니까 7글자로 출력됨
print("###%5d###" %(value))
print("###%10d###" %(value))
print("###%1d###" %(value))

# 리스트에서도 적용할 수 있다는 소리인데
price = [30,13500,2000]
for p in price:
    print("가격 : %d원" %(p))

# %7d : 왼쪽부터 공백을 채운다.
for p in price:
    print("가격 : %7d원" %(p))

# %-7d : -7이니까 오른쪽부터 공백을 채운다.
for p in price:
    print("가격:%-7d원" % p)

#  precision
pie = 3.14159265
# 10글자
print("%10f" % pie)
# 10글자, 소수점 8글자
print("%10.8f" % pie)
# 10글자, 소수점 5글자
print("%10.5f" % pie)
# 10글자, 소수점 2글자
print("%10.2f" % pie)

#  newformat
# 이런 시발 %랑 공백 채우는 규칙이 다른것같은데.. 쓰지마 ㅅㅂ
# 그냥 %d, %()로쓰자
# .format() 이라는 함수를 사용하여 입력받은 변수 값을
# 문자열의 {}에 집어 넣어준다는 소리인데..
name = "석현"
age = 16
height = 162.5
print("이름:{}, 나이:{}, 키:{}".format(name, age, height))

#  newformat2
name = "석현"
age = 16
height = 162.5
print("이름:{0:s}, 나이:{1:d}, 키:{2:f}".format(name, age, height))

#  newformat3
name = "석현"
age = 16
height = 162.5
# s: string, d : 정수 , f : 실수
# 10s : 
print("이름:{0:10s}, 나이:{1:5d}, 키:{2:8.2f}".format(name, age, height))

#  newformat4
name = "석현"
age = 16
height = 162.5
print("이름:{0:^10s}, 나이:{1:>5d}, 키:{2:<8.2f}".format(name, age, height))

#  newformat5
name = "석현"
age = 16
height = 162.5
print("이름:{0:$^10s}, 나이:{1:>05d}, 키:{2:!<8.2f}".format(name, age, height))