import sqlite3

import pandas

conn = sqlite3.connect("./sql/employee.db")

cur = conn.cursor()
cur.execute("SELECT * FROM employee_data")

rows = cur.fetchall() # .fetchall() 쿼리문의 결과의 모든데이터를 가져올때 사용
cols = [column[0] for column in cur.description]
data_df = pandas.DataFrame.from_records(data=rows, columns=cols)
conn.close()
print(data_df)

