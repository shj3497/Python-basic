def my_func():
    print("My first Function!!")
    print("This is a function")
my_func()
print()
def my_friend(friendName):
    print("{}는 나의 친구입니다." .format(friendName))
my_friend("심혁진")
print()
# 인자는 있으나 반환값이 없는 함수
def my_student_info(name, school_ID, phoneNumber):
    print("------------------")
    print("-학생이름 : ", name)
    print("-학급번호 : ", school_ID)
    print("-전화번호 : ", phoneNumber)
my_student_info("현아", "01", "01-235-6789")
print()
# 인자도 있고 반환값도 있는 함수
def my_calc(x,y):
    z=x*y
    return z
print(my_calc(3,4))
print()
def my_student_info_list(student_info):
    print("************")
    print("* 학생이름 : ", student_info[0])
    print("* 학급번호 : ", student_info[1])
    print("* 전화번호 : ", student_info[2])
    print("************")
student1_info = ["현아", "01", "01-235-6789"]
my_student_info_list(student1_info)
print()
# 변수의 유효 범위
a = 5 # 전역변수
def func1():
    a = 1
    print("[func1] 지역변수 a=", a)
def func2():
    a = 2
    print("[func2] 지역변수 a=",a)
def func3():
    print("[func3] 전역변수 a=",a)
def func4():
    global a # 함수 내에서 젼역변수를 변경하기 위해 선언
    a = 4
    print("[func4] 전역변수 a=",a)
func1()
func2()
func3()
func4()
print()

# 람다함수
# lambda <인자> : <인자 활용 수행 코드>
# (lambda <인자> : <인자 활용 수행 코드>)(<인자>)
# lambda_function = lambda <인자> : <인자 활용 수행 코드>
# lambda_function(<인자>)
(lambda x: x**2)(3)
print((lambda x: x**2)(3))
print()
mySquare = lambda x:x**2
print(mySquare(2))
print(mySquare(5))
print()
mySimpleFunc = lambda x,y,z : 2*x + 3*y + z
print(mySimpleFunc(1,2,3))
# 흠.. lambda x : 함수식 ㅇㅋ
print()

# 유용한 내장 함수
# 형변환 함수
data1 = [int(0.123), int(3.541592), int(-1.812)]
print(data1) # 음수는 반올림을 하네? 양수는 내림하고
data2 = [float(0), float(123), float(-567)]
print(data2)
print()
# 문자형으로 변환
data3 = [str(0), str(123), str(-567)]
print(data3)
print()

# 리스트, 튜플, 세트형으로 변환
list_data = ['abc',1,2,'def']       # 요소를 삭제하거나 변경 O
tuple_data = ('abc',1,2,'def')      # 요소를 삭제하거나 변경 X
set_data = {'abc',1,2,'def'}        # 요소의 중복이 불가능
data4 = [type(list_data), type(tuple_data), type(set_data)]
print(data4)
print("리스트로 변환", list(tuple_data), list(set_data))
print("튜플로 변환", tuple(list_data), tuple(set_data))
print("셋으로 변환", set(tuple_data), set(list_data))
print()

# bool 함수
print(bool(0)) # false
print(bool(1)) # true
print(bool(-10)) # true # 0이외의 숫자를 입력하면 모두 True를 반환
print()
# 문자열을 인자로 bool 함수 호출
# 공백이면 False, 문자열이 존재하면 모두 True를 반환
print(bool('a')) # True
print(bool('')) # False
print()

# 리스트, 튜플, 세트를 인자로 bool 함수 호출
myFriends = []
print(bool(myFriends)) # 리스트에 값이 null 이면 False
myFriends = [1,2,3]
print(bool(myFriends)) # True
# 튜플, 세트도 값이 null 이면 False, 존재하면 True
print()

# bool 함수의 활용
def print_name(name):
    if(bool):
        print("입력된 이름 : ", name)
    else:
        print("입력된 이름이 없습니다.")
print_name("James")

# 최댓값과 최솟값을 구하는 함수
mynum = [10,5,12,0,3.5,99.5,42]
print([min(mynum), max(mynum)])
# 절댓값
print([abs(10), abs(-10)])
# 내장함수 sum()
print(sum([1,2,3,4,5,6,7,8,9,10]))
print()

# 항목의 개수를 구하는 함수
print(len("ab cd"))
print(len([1,2,3,4,5,6,7,8]))
print(len((1,2,3,4,5)))
print(len({'a','b','c','d'}))
print(len({1:"1",2:"2",3:"3"}))
print()

# 내장함수의 활용
scores=[90,80,95,85] # 과목별 시험 점수
score_sum = 0
subject_num = 0
for score in scores:
    score_sum = score_sum + score # 과목별 점수 모두 더하기
    subject_num = subject_num + 1 # 과목수 계산
average = score_sum / subject_num # 평균
print("총점:{0}, 평균:{1}".format(score_sum, average))
print()
print("총점:{0}, 평균:{1}".format(sum(scores), sum(scores)/len(scores)))
print()
print("최하점수:{0}, 최고점수:{1}".format(min(scores),max(scores)))