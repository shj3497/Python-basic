import pandas

data1 = {'name' : [ 'Jerry', 'Riah', 'Paul'],
         'algol' : [ "A", "A+", "B"],
         'basic' : [ "C", "B", "B+"],
          'c++' : [ "B+", "C", "C+"]}

data2 = {'c0':[1,2,3],
         'c1':[4,5,6],
         'c2':[7,8,9],
         'c3':[10,11,12],
         'c4':[13,14,15]}

df1 = pandas.DataFrame(data1)
print(df1)
print("\n")
df1.set_index('name', inplace=True) # name열을 인덱스로 지정
print(df1)
print("\n")

df2 = pandas.DataFrame(data2)
print(df2)
print("\n")
df2.set_index('c0', inplace=True)
print(df2)

# df1을 'sheet1'으로, df2를 'sheet2'로 저장
# sheet_name 옵션으로 sheet 번호를 지정해서 저장 가능하다.
writer = pandas.ExcelWriter("./data/df_excelwriter.xlsx") # 경로
df1.to_excel(writer, sheet_name="sheet1")
df2.to_excel(writer, sheet_name="sheet2")
writer.save()