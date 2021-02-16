import random

import matplotlib
import matplotlib.pyplot as plt
import numpy
import pandas

# pandas로 그래프 그리기
# Series_data.plot([kind='graph_kind'][,option])
# DataFrame_data.plot([x=label or position, y=label or position,][kind='graph_kind' [, option]])

"""
s1 = pandas.Series([1,2,3,4,5,6,7,8,9,10], index=pandas.date_range('2021-02-16', periods=10))
print(s1)
s1.plot()
s1.plot(grid=True)
# 판다스 에서는 Series에서 바로 plot() 하네..
# matplotlib.pyplot as plt 로 해서 했는데..
# show는 plt로 함
plt.show()
"""

# 직선그래프
"""
df_rain = pandas.read_csv('./data/sea_rain1.csv', index_col='연도')
print(df_rain)

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

#df_rain.plot() 그래프를 그린다.

rain_plot = df_rain.plot(grid=True, style=['r-*','g-o','b:*','m-.p'])
rain_plot.set_xlabel('연도')
rain_plot.set_ylabel('강수량')
rain_plot.set_title('연간 강수량')
plt.show()
"""

# 직선 그래프
"""
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False
year = numpy.arange(2006,2018,2)
area = [26.2, 27.8, 28.5, 31.7, 33.5, 33.2]
table = {'연도':year, '주거면적':area}
df_area = pandas.DataFrame(table, columns=['연도','주거면적'])
print(df_area)
df_area.plot(x='연도', y='주거면적', grid=True, title='연도별 1인당 주거면적')
plt.show()
"""

# 산점도
"""
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

template = [25.2, 27.4, 22.9, 26.2, 29.5, 33.1, 30.4, 36.1, 34.4, 29.1]
Ice_cream_sales = [236500, 357500, 203500, 365200, 446600, 574200, 453200, 675400, 598400, 463100]
dict_data = {'기온':template, '아이스크림 판매량':Ice_cream_sales}
df_ice_cream = pandas.DataFrame(dict_data, columns=['기온','아이스크림 판매량'])

print(df_ice_cream)

df_ice_cream.plot.scatter(x='기온', y='아이스크림 판매량', grid=True, title="최고기온과 아이스크림 판매량")
plt.show()
"""


# 막대그래프
"""
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

grade_num = [5,14,13,3]
students = ['A','B','C','D']

df_grade = pandas.DataFrame(grade_num, index=students, columns=['Student'])
print(df_grade)

grade_bar = df_grade.plot.bar(grid=True)
grade_bar.set_xlabel("학점")      # matplotlib.pyplot 은 plt.xlabel()로 해줌
grade_bar.set_ylabel("학생수")     # pandas.plot 은 .set_xlabel()로 해줌
grade_bar.set_title("학점별 학생 수 막대 그래프")
plt.show()
"""

# 히스토그램
"""
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False
def random_List(size):
    result = []

    for i in range(size):
        result.append(random.randint(60,100))
    return result

math = []
math = random_List(30)
print(math)

df_math = pandas.DataFrame(math, columns=['Student'])
math_hist = df_math.plot.hist(bins=8, grid=True)
math_hist.set_xlabel('시험점수')
math_hist.set_ylabel('도수(frequency)')
math_hist.set_title("수학시험의 히스토그램")
plt.show()
"""

# 파이그래프
"""
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False
fruit = ['사과','바나나','딸기','오렌지','포도']
result = [7,6,3,2,2]

df_fruit = pandas.Series(result, index=fruit, name='선택한 학생수')
print(df_fruit)

df_fruit.plot.pie(autopct="%.1f%%")
plt.show()
"""