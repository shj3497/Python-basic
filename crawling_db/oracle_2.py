import cx_Oracle
import pandas

dsn = cx_Oracle.makedsn("localhost", 1521, "orclSHJ00")
print(dsn)

db = cx_Oracle.connect("scott","tiger", dsn)
print(db)

cursor = db.cursor()
cursor.execute("SELECT * FROM EMP")
data = cursor.fetchall()
df = pandas.DataFrame(data)
print(df)
