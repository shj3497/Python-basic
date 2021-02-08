import sqlite3

conn = sqlite3.connect('./sql/employee.db')
cur = conn.cursor()
cur.execute("select * FROM employee_data")

# cursor().fetchall() : 모든 데이터를 한꺼번에 가져올 때 사용된다.
# cursor().fetchone() : 한번 호출에 하나의 Row만을 가져올 때 사용된다.
# cursor().fetchmany(n) : n개만큼의 데이터를 한꺼번에 가져올때 사용..
rows = cur.fetchall()
print("### rows ###")
print(rows)
print()
for row in rows:
    print(row)
conn.close()
