import cx_Oracle

# 오라클 데이터베이스 SID 찾아서 연걸하기
import pandas

dsn = cx_Oracle.makedsn("localhost", 1521, 'orclSHJ00')
print(dsn)

# 오라클 데이터베이스에서 사용할 테이블 연결
db = cx_Oracle.connect("scott", "tiger", dsn)
print(db)

# 실행 메모리 영역(cursor) 열기
cursor = db.cursor()

# 데이터 조회
cursor.execute("SELECT * FROM EMP")
data = cursor.fetchall()
df = pandas.DataFrame(data)

# 컬럼 정보 조회
cursor.execute("""
    SELECT COLUMN_NAME
    FROM USER_TAB_COLUMNS
    WHERE TABLE_NAME = 'EMP'
""")
col = cursor.fetchall()
df.columns = col # pandas.DataFrame.columns : 행 이름 설정
print(df.columns)

# 튜플이 내장된 리스트 형식으로 출력하기
col_new = [j for i in col for j in i] # >>> ?????
df.columns = col_new
print(df.columns)
print()
"""
print(df)
cursor.close()
db.close()
"""