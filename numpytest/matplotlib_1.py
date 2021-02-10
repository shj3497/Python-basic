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

# plt.subplot(m,n,p)
x = numpy.arange(0,10,0.1)
y1 = 0.3*(x-5)**2 + 1
y2 = -1.5*x + 3
y3 = numpy.sin(x)**2 # Numpy에서 sin()은 numpy.sin()으로 입력
y4 = 10*numpy()