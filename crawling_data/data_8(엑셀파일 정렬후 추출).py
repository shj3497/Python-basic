import openpyxl

filename = "./file/stats_104102.xlsx"
# 엑셀파일을 불러올 때는 openpyxl.load_workbook(filename)으로 불러온다.
book = openpyxl.load_workbook(filename)

# 불러온 엑셀파일의 시트를 선택할 수 있음
# .worksheets[0]
sheet = book.worksheets[0]

data=[]

# sheet.rows 열을 기준으로 시작
for row in sheet.rows:
    data.append([
        row[0].value,   # 계
        row[10].value   # 2018년
    ])
print(data)
del data[0] # 1행 '시도별 인구 변동 현황[단위 : 천명] 도 data에 들어가있으므로 삭제
del data[1] # 2행 [None, 2018] 삭제
del data[2] # 3행 ['계', 51826] 삭제
# 실질적인 data는 4행부터 시작하므로 1,2,3행은 삭제해준다.
print()
print(data)

# 인구변동이 가장 적은 단위로 정렬한후 출력
# sorted : 정렬
data = sorted(data, key=lambda x:x[1])

# 인덱스 추가
for i, a in enumerate(data):
    if(i>=5): break
    print(i+1, a[0], int(a[1]))

