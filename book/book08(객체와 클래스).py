class Bicycle(): # 클래스선언
    pass
my_bicycle = Bicycle()
print(my_bicycle)
my_bicycle.wheel_size = 26
my_bicycle.color = 'black'
print("바퀴의 크기 : ", my_bicycle.wheel_size) # 객체의 속성 출력
print("색상 : ", my_bicycle.color)
print()

# 객체 생성 및 활용
class Bicycle():
    # 클래스 함수 안에서는 'self.변수명 = 속성값' 으로 속성값을 설정하고
    # self.변수명 으로 속성값을 가져온다.
    # >> 클래스 안에서의 변수 사용 self.변수명
    # >> 외부에서 변수 사용 클래스명.변수명
    def move(self, speed):
        print("자전거 : 시속 {0}킬로미터로 전진".format(speed))

    def turn(self, direction):
        print("자전거 : {0}회전".format(direction))

    def stop(self):
        print("자전거({0}, {1}) : 정지".format(self.wheel_size,self.color))

my_bicycle = Bicycle() # Bicycle 클래스의 인스턴스인 my_bicycle 객체 생성
my_bicycle.wheel_size = 26
my_bicycle.color = 'black'
print(my_bicycle.move(30))
print(my_bicycle.turn('좌'))
print(my_bicycle.stop())
print()

bicycle1 = Bicycle()
bicycle1.wheel_size = 27
bicycle1.color = 'red'
print(bicycle1.move(20))
print(bicycle1.turn('우'))
print(bicycle1.stop())
print()

bicycle2 = Bicycle()
bicycle2.wheel_size = 24
bicycle2.color = 'blue'
print(bicycle2.move(15))
print(bicycle2.turn('우'))
print(bicycle2.stop())
print()

# 객체 초기화
# __init__()
# __init__() 이 없을 때는 객체(my_bicycle)를 생성하고
# 속성값을 지정해서 넣어주어야 했는데
# __init__() 함수가 정의되어 있으면 Bicycle()객체를 생성할 때
# 속성값을 지정해서 초기화 해준다.
class Bicycle():
    def __init__(self, wheel_size, color):
        self.wheel_size = wheel_size
        self.color = color
    def move(self, speed):
        print("자전거 : 시속 {0}킬로미터로 전진".format(speed))

    def turn(self, direction):
        print("자전거 : {0}회전".format(direction))

    def stop(self):
        print("자전거({0}, {1}) : 정지".format(self.wheel_size,self.color))
print("__init__() 함수 지정")
my_bicycle = Bicycle(26,'black')
print(my_bicycle.move(30))
print(my_bicycle.turn('좌'))
print(my_bicycle.stop())
print()

# 클래스에서 사용하는 변수
class Car():
    instance_count = 0 # 클래스 변수 생성 및 초기화
    def __init__(self, size, color):
        self.size = size
        self.color = color
        Car.instance_count = Car.instance_count + 1 # 클래스 변수 이용
        print("자동차 객체의 개수 : {0}".format(Car.instance_count))

    def move(self):
        print("자동차({0} & {1})가 움직입니다.".format(self.size, self.color))
car1 = Car('small','white')
car2 = Car('big','black')
print("Car 클래스의 총 인스턴스 개수 :{}".format(Car.instance_count))
print()
print("Car 클래스의 총 인스턴스 개수 :{}".format(car1.instance_count))
print("Car 클래스의 총 인스턴스 개수 :{}".format(car2.instance_count))
# car1객체와 car2객체에서 사용한 클래스변수 instance_count 는 값이 같은 것을 볼 수 있다.
# 이는 모든 객체에서 클래스 변수가 공통으로 사용되기 때문이다.
print(car1.move())
print(car2.move())
print()

class Car2():
    count = 0
    def __init__(self, size, num):
        self.size = size
        self.count = num # 인스턴스 변수 생성 및 초기화
        Car2.count = Car2.count + 1 # 클래스 변수를 이용한다.
        print("자동차 객체의 수 : Car2.count={0}".format(Car2.count))
        print("인스턴스 변수 초기화 : self.count = {0}".format(self.count))

    def move(self):
        print("자동차({0}, {1}) 가 움직입니다.".format(self.size, self.count))
car1 = Car2("big",20)
car2 = Car2("small", 30)
# 위의 결과는 클래스변수 count와 인스턴스변수 count가 별도로 동작하는것을 보여준다.
print()

# 클래스에서 사용하는 함수
# 1. 인스턴스 메소드 : 각 객체에서 개별적으로 동작하는 함수
#   첫 인자로 self가 필요
# Car 클래스 선언
class Car():
    instance_count = 0 # 클래스 변수 생성 및 초기화
    # 초기화 함수(인스턴스 메소드)
    def __init__(self, size, color):
        self.size = size
        self.color = color # 인스턴스 변수 생성 및 초기화
        Car.instance_count = Car.instance_count+1 # 클래스 변수 이용
        print("자동차 객체의 수 :{0}".format(Car.instance_count))
    # 인스턴스 메소드
    def move(self,speed):
        self.speed = speed # 인스턴스 변수 생성
        print("자동차({0} & {1})가".format(self.size, self.color), end="")
        print("시속{0}킬로미터로 전진.".format(self.speed))
    
    # 인스턴스 메소드
    def auto_cruise(self):
        print("자율 주행 모드")
        self.move(self.speed) # move()함수의 인자로 인스턴스 변수를 입력
car1 = Car("small","red") # 객체생성(car1)
car2 = Car("big","green") # 객체생성(car2)
car1.move(80) # car1의 move() 메소드 호출
car2.move(100) # car2의 move() 메소드 호출
car1.auto_cruise() # 객체(car1)의 auto_cruise() 메소드 호출
car2.auto_cruise() # 객체(car2)의 auto_cruise() 메소드 호출
# auto_cruise()에서 self.함수명()을 이용해 인스턴스 메소드 호출함
print()
# 2. 정적 메소드

class Car():
    instance_count = 0  # 클래스 변수 생성 및 초기화

    # 초기화 함수(인스턴스 메소드)
    def __init__(self, size, color):
        self.size = size
        self.color = color  # 인스턴스 변수 생성 및 초기화
        Car.instance_count = Car.instance_count + 1  # 클래스 변수 이용
        print("자동차 객체의 수 :{0}".format(Car.instance_count))

    # 인스턴스 메소드
    def move(self, speed):
        self.speed = speed  # 인스턴스 변수 생성
        print("자동차({0} & {1})가".format(self.size, self.color), end="")
        print("시속{0}킬로미터로 전진.".format(self.speed))

    # 인스턴스 메소드
    def auto_cruise(self):
        print("자율 주행 모드")
        self.move(self.speed)  # move()함수의 인자로 인스턴스 변수를 입력

    # 정적 메소드
    @staticmethod
    def check_type(model_code):
        if(model_code >= 20):
            print("이 자동차는 전기차 입니다.")
        elif(10 <= model_code < 20):
            print("이 자동차는 가솔린차 입니다.")
        else:
            print("이 자동차는 경유차 입니다.")

# 3. 클래스 메소드
