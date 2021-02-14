import pandas

# header = 0 (default 옵션)
df1 = pandas.read_excel("./data/남북한발전전력량.xlsx")

# header = None 옵션
df2 = pandas.read_excel("./data/남북한발전전력량.xlsx", header=None)

# 데이터 프레임 출력
print(df1) # header=0(default) 옵션이면 엑셀에 적용된 모델 그대로 출력
print("\n")
print(df2) # header=None 옵션을 달면 열에도 인덱스가 달림