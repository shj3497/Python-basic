import pandas

filename = "./file/stats_104102.xlsx"
sheet_name = "stats_104102" #엑셀파일 안에서 시트를 불러올 수 있다
book = pandas.read_excel(filename, sheet_name=sheet_name, header = 1) # 첫 번째줄부터 헤더

# 2018년 인구로 정렬
book = book.sort_values(by=2018, ascending=False)
print(book)
