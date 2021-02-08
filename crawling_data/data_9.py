import openpyxl

filename="./file/stats_104102.xlsx"
# 엑셀을 읽어올 때는 openpyxl.load_workbook()으로 불러온다.
book = openpyxl.load_workbook(filename)

# 활성화된 시트 추출하기
sheet = book.active
# 서울을 제외한 인구를 구해서 쓰기
for i in range(0,10):
    # str(chr(i+66)) : ascii코드로 변환해서 열을 의미하는것 같은데?
    # "3" : 시트 행을 말하는거일테고..
    # sheet[열 + 행] ?
    total = int(sheet[str(chr(i + 66)) + "3"].value)
    seoul = int(sheet[str(chr(i + 66)) + "4"].value)
    output = total - seoul
    print("서울 제외 인구 = ", output)
    # 쓰기
    sheet[str(chr(i+66)) + "21"] = output
    cell = sheet[str(chr(i+66)) + "21"]
    # 폰트와 색상 변경해보기
    cell.font = openpyxl.styles.Font(size=14, color="FF0000")
    cell.number_format = cell.number_format
# 엑셀 파일 저장히기
filename = "./file/population.xlsx"
book.save(filename)
print("ok")