import sqlite3

"""
Sqlite3 데이터 타입
--------------------
파이썬      SQLite
None        NULL
int         INTEGER
float       REAL
str         TEXT
bytes       BLOB
"""
# 모듈을 사용하려면 데이터베이스를 나타내는 Connection 객체를 만들어야한다.
# 모든 데이터는 .db파일에 저장됨
# conn = sqlite3.connect()로 Connection 객체를 얻는다.
#       connect("aaa.db") : aaa.db라는 파일이 없으면 생성하여 연결하는듯?

# cur = conn.cursor() : Connection을 얻으면 Cursor 객체를 만들고
conn = sqlite3.connect("./sql/employee_1.db")
cur = conn.cursor()

# conn.execute() : execute()메소드를 호출하여 SQL 명령 수행
# conn의 .execute()로 CREATE하는것에 주의해아할듯?
# cur.execute('CREATE TABLE employee_data(id INTEGER, name TEXT, nickname TEXT, department TEXT, employment_date TEXT)')
# cursor 객체에 만드는것도 가능한데 차이가 뭔지는 모르겠음
conn.execute('CREATE TABLE employee_data(id INTEGER, name TEXT, nickname TEXT, department TEXT, employment_date TEXT)')
# 이러면 안될 것같다.


# cursor().execute() : 스트링으로 입력하는 듯
# cursor().executemany() : 리스트, 튜플, 딕셔너리로 입력하는 듯
# 여기서는 배열안에 튜플을 선언해서 넣었다.
cur.executemany('INSERT INTO employee_data VALUES(?,?,?,?,?)',
                [(1001, 'Donghyun', 'SOMJANG', 'Development', '2020-04-01 00:00:00.000'),
                 (2001, 'Sol', 'Fairy', 'Marketing', '2020-04-01 00:00:00.000'),
                 (2002, 'Jiyoung', 'Magician', 'Marketing', '2020-04-01 00:00:00.000'),
                 (1002, 'Hyeona', 'Theif', 'Development', '2020-04-01 00:00:00.000'),
                 (1003, 'Soyoung', 'Chief', 'Development', '2020-04-01 00:00:00.000')])
conn.commit()
conn.close()
