# 데이터 파일을 읽고 쓰기
# DataFrame_data = pandas.read_csv(file_name [, options])
# CSV : Comma-Separated Values : 각 데이터가 콤마로 구분
import codecs
import csv

import pandas

sea_rain1 = pandas.read_csv("./data/sea_rain1.csv")
print(sea_rain1)
# pandas.read_csv("~.csv", encoding="UTF-8")
print()
print()

sea_rain1_space = pandas.read_csv("./data/sea_rain1_space.csv", sep=" ")
print(sea_rain1_space)
# sep=" " 라는 옵션으로 csv에서 ,가 아닌 공백을 기준으로 해주었다.

sea_rain1_1 = pandas.read_csv("./data/sea_rain1.csv", index_col="연도")
print(sea_rain1_1)
print()
print()


# 표 형식의 데이터 파일로 쓰기
# DataFrame_data.to_csv(file_name [, options])
df_WH = pandas.DataFrame({'Weight':[62,67,55,74],
                          'Height':[165,177,160,180]},
                           index=['ID_1','ID_2','ID_3','ID_4'])
df_WH.index.name='User'
print(df_WH)
bmi = df_WH['Weight'] / (df_WH['Height']/100)**2
print(bmi)

# print(df_WH.join(bmi)) 
# >>> join은 컬럼을 집어넣는거지..
# 위에서 구한 bmi는 행렬의 연산값이지 현재는 컬럼이 아니다.
# 그래서 df_WH["BMI"] 라는 'key' 값을 만들어주고 연산의 결과(bmi) 'value' 값을 넣어주는것
df_WH['BMI'] = bmi
print(df_WH)
print()
df_WH.to_csv("./data/save_DataFrame.csv")
# 파일을 쓰기위해서 .to_csv()라는것을 쓸 수도 있고
# with open()이라는 함수도 있다.

df_pr = pandas.DataFrame({'판매가격':[2000,3000,5000,10000],
                          '판매량':[32,53,40,25]},
                          index=['P1001','P1002','P1003','P1004'])
df_pr.index.name='제품번호'
print(df_pr)
print()
file_name = "./data/save_DataFrame_cp949.txt"
df_pr.to_csv(file_name, sep=" ", encoding="UTF-8") # encoding="cp949"