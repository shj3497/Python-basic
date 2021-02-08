import codecs

# EUC-KR로 저장된 csv파일 읽기
filename = "./file/list-euckr.csv"
# 인코딩 주의
csv = codecs.open(filename,'r', encoding="euc-kr").read()
# CSV을 파이썬 리스트로 변환하기
data = []
rows = csv.split("\r\n")
for row in rows:
    if row == "":
        continue
    cells = row.split(",")
    data.append(cells)
# 결과 출력하기
for c in data:
    print(c[1],c[2])
print(data)