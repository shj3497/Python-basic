import cx_Oracle
import pandas

dsn = cx_Oracle.makedsn("localhost", 1521, 'orclSHJ00')
print(dsn)

db = cx_Oracle.connect("scott", "tiger", dsn)
print(db)

cursor = db.cursor() # cursor()로 db동작 시작같은 느낌
cursor.execute("SELECT * FROM EMP") # .execute("") 쿼리문 작성
data = cursor.fetchall() # .fetchall() : 쿼리문 실행
print(data)
df = pandas.DataFrame(data)
print(df)

cursor.close()
db.close()
