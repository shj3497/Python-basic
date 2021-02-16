import matplotlib
import matplotlib.pyplot as plt
import numpy

# 선그래프
# 주석 풀으면서 확인할것

data1 = [10,14,19,20,25]
print(data1)

#plt.plot(data1)
#plt.show()

x = numpy.arange(-4.5,5,0.5) # 배열 x생성
y = 2*x**2 # 수식을 이용해서 배열 x에 대응하는 배열 y 생성
print([x,y])
#plt.plot(x,y)
#plt.show()
print()

x = numpy.arange(-4.5,5,0.5)
y1 = 2*x**2
y2 = 5*x + 30
y3 = 4*x**2 + 10
"""
plt.plot(x,y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()
"""
#plt.plot(x,y1, x,y2, x,y3)
#plt.show()
"""
plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.figure()
plt.plot(x, y3)
plt.show()
"""
x = numpy.arange(-5,5,0.1)
y1 = x**2 -2
y2 = 20*numpy.cos(x)**2

"""
plt.figure(1) # 1번 그래프 창을 생성
plt.plot(x,y1) # 지정된 그래프 창에 그래프를 그린다.

plt.figure(2) # 2번 그래프 창을 지정
plt.plot(x,y2) # 지정된 그래프 창에 그래프를 그린다.

plt.figure(1) # 이미 생성된 그래프 창을 지정
plt.plot(x,y2) # 지정된 그래프 창에 그래프를 그린다.(추가로)

plt.figure(2) # 이미 생성된 그래프 창을 지정
plt.clf() # 지정된 그래프 창에 그려진 모든 그래프를 지운다.!! (.clf())
plt.plot(x,y1) # 지정된 그래프 창에 그래프를 그린다.
plt.show()
"""

"""
# plt.subplot(m,n,p)
x = numpy.arange(0,10,0.1)
y1 = 0.3*(x-5)**2 + 1
y2 = -1.5*x + 3
y3 = numpy.sin(x)**2 # Numpy에서 sin()은 numpy.sin()으로 입력
y4 = 10*numpy.exp(-x) + 1 # Numpy에서 exp()는 numpy.exp()으로 입력

# 2*2 행렬로 이루어진 하위 그래프에서 p에 따라 위치를 지정한다.
plt.subplot(2,2,1) # p=1
plt.plot(x, y1)

plt.subplot(2,2,2) # p=2
plt.plot(x, y2)

plt.subplot(2,2,3) # p=3
plt.plot(x, y3)

plt.subplot(2,2,4) # p=4
plt.plot(x, y4)

plt.show()
# 결과를 보면 4개의 그래프가 각각 subplot() 으로 지정한위치에 잘 그려진것을 볼 수 있다.
"""

# 그래프의 출력 범위 지정하기
# plt.xlim(xmin, xmax) # x축의 좌표 범위 지정(xmin ~ xmax)
# plt.ylim(ymin, ymax) # y축의 좌표 범위 지정(ymin ~ ymax)
# [xmin, xmax] = plt.xlim() # x 축의 좌표 범위 가져오기
# [ymin, ymax] = plt.ylim() # y 축의 좌표 범위 가져오기
"""
x = numpy.linspace(-4,4,100) # [-4,4] 범위에서 100개의 값을 생성한다.
y1 = x**3
y2 = 10*x**2 -2

plt.plot(x,y1)
plt.plot(x,y2)
# x,y값의 범위를 지정해준다.
plt.xlim(-1,1)
plt.ylim(-3,3)
plt.show()
"""

# 그래프 꾸미기
# fmt = '[color][line_style][marker]'
"""
x = numpy.arange(0,5,1)
y1 = x
y2 = x+1
y3 = x+2
y4 = x+3

plt.plot(x,y1, color='m', linestyle="-") #magenta
plt.plot(x,y2, color="y", linestyle="--") #yellow
plt.plot(x,y3, color="k", linestyle=":") #black
plt.plot(x,y4, color='c', linestyle="-.") #cyan
plt.show()
"""

# 라벨 제목 격자 범례 문자열 표시
"""
x = numpy.arange(-4.5, 5, 0.5)
y = 2*x**3
plt.plot(x,y)
plt.title('Graph Title')
plt.xlabel('X-axis') # x축에 라벨로 문자열을 추가한다.
plt.ylabel('Y-axis') # y축에 라벨로 문자열을 추가한다.
plt.grid(True)
plt.show()
"""

"""
x = numpy.arange(0,5,1)
y1 = x
y2 = x+1
y3 = x+2
y4 = x+3

plt.plot(x,y1,'>-r', x,y2,'s-g', x,y3,'d:b', x,y4,'-.Xc')
plt.legend(['data1','data2','data3','data4'], loc=4)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph title')
plt.grid(True)
plt.show()
"""

# 만약 그래프에서 한글을 표시하고 싶다면 matplotlib에서 사용하는 폰트를 한글 폰트로 지정해야한다.
# import matplotlib
# matplotlib.rcParams['font.family']
# 폰트를 변경하지 않았다면 기본 폰트는 sans-serif 이다.
# 폰트 변경하는 방법
# matplotlib.rcParams['font.family'] = '폰트이름'
# matplotlib.rcParams['axes.unicode_minus'] = False

"""
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 맑은 고딕으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 폰트가 깨지는것을 막아준다.
x = numpy.arange(0,5,1)
y1 = x
y2 = x+1
y3 = x+2
y4 = x+3

plt.plot(x,y1,'>-r', x,y2,'s-g', x,y3,'d:b', x,y4,'-.Xc')
plt.text(0,6,"문자열 출력1") # 좌표값 (0,6) 위치에서 해당 문자열이 출력됨
plt.text(0,5,"문자열 출력2")
plt.text(3,1,"문자열 출력3")
plt.text(3,0,"문자열 출력4")
plt.show()
"""

# 산점도
# plt.scatter(x,y [,s=size_n, c=colors, marker='marker_string', alpha=alpha_f])
"""
matplotlib.rcParams['font.family'] = "Malgun Gothic"
matplotlib.rcParams['axes.unicode_minus'] = False
height = [165,177,160,180,185,155,172] # 키 데이터
weight = [62,67,55,74,90,43,64] # 몸무게 데이터
plt.scatter(height, weight, s=500, c='r') # scatter(x,y) 해줌
plt.xlabel('키(cm)')
plt.ylabel('몸무게(kg)')
plt.title("키 & 몸무게")
plt.grid(True)
plt.show()
"""

"""
matplotlib.rcParams['font.family'] = "Malgun Gothic"
matplotlib.rcParams['axes.unicode_minus'] = False
height = [165,177,160,180,185,155,172] # 키 데이터
weight = [62,67,55,74,90,43,64] # 몸무게 데이터

size = 100*numpy.arange(1,8)
colors=['r','g','b','c','m','k','y'] # 데이터별로 마커의 컬러 지정
plt.scatter(height,weight,c=colors,s=size)
plt.show()
"""

"""
matplotlib.rcParams['font.family'] = "Malgun Gothic"
matplotlib.rcParams['axes.unicode_minus'] = False

city = ['서울','인천','대전','대구','울산','부산','광주']

# 위도와 경도
lat = [37.56, 37.45, 36.35, 35.87, 35.53, 35.18, 35.16]
lon = [126.97, 126.70, 127.38, 128.60, 129.31, 129.07, 126.85]

# 인구밀도(명/km^2) : 2017년 통계청 자료
pop_den = [16154, 2751, 2839, 2790, 1099, 4454, 2995]

size = numpy.array(pop_den) * 0.5 # 마커의 크기 지정
colors = ['r','g','b','c','m','k','y']

plt.scatter(lon,lat, s=size, c=colors, alpha=0.5)
plt.xlabel('경도(longgitude)')
plt.ylabel('위도(latitude)')
plt.title('지역별 인구 밀도(2017)')

for x,y,name in zip(lon,lat,city):
    plt.text(x,y,name) # 위도 경도에 맞게 도시 이름 입력했음
plt.show()
"""

# 막대그래프
# plt.bar(x, height [,width=width_f, color=colors, tick_label=tick_labels, align='center'(기본) or 'edge', label=labels])
"""
member_IDs = ['m_01', 'm_02', 'm_03', 'm_04'] # 회원 ID
before_ex = [27,35,40,33]
after_ex = [30,38,42,37]
colors = ['r','g','b','m']

n_data = len(member_IDs)
index = numpy.arange(n_data)
#plt.bar(index, before_ex) # bar(x,y)에서 x=index, height=before_ex로 지정
plt.barh(index, before_ex, tick_label=member_IDs, color=colors) # x축의 tick 라벨을 member_IDs로 지정했다.
plt.show()
"""

"""
plt.rcParams['font.family'] = 'Malgun Gothic'
member_IDs = ['m_01', 'm_02', 'm_03', 'm_04'] # 회원 ID
before_ex = [27,35,40,33]
after_ex = [30,38,42,37]
colors = ['r','g','b','m']

n_data = len(member_IDs)
index = numpy.arange(n_data)

barWidth = 0.4
plt.bar(index, before_ex, color='c', align='edge', width=barWidth, label='before')
plt.bar(index+barWidth, after_ex, color='m', align='edge', width=barWidth, label='after')
plt.xticks(index+barWidth, member_IDs)
plt.legend(loc=2)
plt.xlabel('회원ID')
plt.ylabel('윗몸일으키기 횟수')
plt.title('운동시작전과 후의 근지구력 변화 비교')
plt.show()
"""

# 히스토그램
# plt.hist(x, [,bins=bins_n or 'auto'])
"""
math = [76,82,84,83,90,86,85,92,72,71,100,87,76,94,78,81,60,79,69,74,87,82,68,79]
plt.hist(math)
plt.show()
"""

# 파이그래프
# plt.pie(x [,labels=label_seq, autopct="비율 표시 형식(ex: %0.1f)',
#           shadow=Flase(기본) or True, explode=explode_seq,
#           counterclock = True(기본) or False, startangle = 각도(기본은 0)])
"""
plt.rcParams['font.family'] = 'Malgun Gothic'
fruit = ['사과','바나나','딸기','오렌지','포도']
result = [7,6,3,2,2]
explode_value=(0.1,0,0,0,0)

plt.figure(figsize=(5,5))
plt.pie(result, labels=fruit, autopct='%.1f%%', startangle=90, counterclock=False
        , explode=explode_value, shadow=True)
plt.show()
"""

# 그래프 저장하기
# plt.savefig(file_name [,dpi = dpi_n(기본은 72)])
"""
x = numpy.arange(0,5,1)
y1 = x
y2 = x+1
y3 = x+2
y4 = x+3

plt.plot(x,y1, x,y2, x,y3, x,y4)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Saving a figure')

# 그래프를 이미지 파일로 저장. dpi는 100으로 설정
# 그래프의 크기를 변경하지 않아서
# 너비 6인치, 높이 4인치로 지정이 되있고
# 너비 600픽셀, 높이 400픽셀인 이미지 파일이 생성된다.
plt.savefig('./data/saveFigTest1.png', dpi=100)
plt.show()
"""

"""
plt.rcParams['font.family'] = 'Malgun Gothic'
fruit = ['사과','바나나','딸기','오렌지','포도']
result = [7,6,3,2,2]
explode_value=(0.1,0,0,0,0)

plt.figure(figsize=(5,5)) # 그래프 크기를 지정(인치)
plt.pie(result, labels=fruit, autopct="%.1f%%", startangle=90, counterclock=False,
        explode=explode_value, shadow=True)
# 그래프를 이미지 파일로 저장. dpi는 100으로 설정
plt.savefig("./data/saveFigTest2.png", dpi=200)
plt.show()
# 픽셀 = 인치*dpi
"""

