import numpy as np
import matplotlib.pyplot as plt
# import numpy as np >> 패키지 numpy를 np라는 명명으로 사용하겠다
data1 = [0, 1, 2, 3, 4]
data2 = ['a', 'b', 'c', 'd']

# numpy.array() 는 배열을 ','를 제외하고 출력할 수 있다.
a1 = np.array(data1)
a2 = np.array(data2)

# 주석
print(a1) # 배열에서, 를 띄고 출력할 수 있다.
print(a1.dtype)
print(type(a1))

print(a2) # 배열에서, 를 띄고 출력할 수 있다.
print(a2.dtype)
print(type(a2))

# matplotlib 패키지 안에있는 pyplot이라는 함수를 plt로 사용하기로 했다.
# matplotlib.pyplot 은 데이터를 시각화 해줌(그래프로)
plt.plot(data1)
plt.show()
print('hello')

data3 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
plt.plot(data3)
plt.show()