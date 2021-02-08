# 데이터 베이스 연결하기
import sqlite3

filepath = "./sql/text2.sqlite"
conn = sqlite3.connect(filepath)

# 테이블 생성하기
cur = conn.cursor()
# 만약 items라는 테이블이 존재하면 지우라.
cur.execute("DROP TABLE IF EXISTS items")
cur.execute("""
            CREATE TABLE items(
                item_id INTEGER PRIMARY KEY,
                name    TEXT,
                price   INTEGER)""")
conn.commit()

# 데이터 넣기
# cursor.execute()
cur = conn.cursor()
cur.execute("INSERT INTO items (name,price) VALUES(?,?)", ("Orange",5200))
conn.commit()

# 여러데이터 연속으로 넣기
# cursor.executemany()
cur = conn.cursor()
data = [("Mango",7700), ("Kiwi",4000), ("Grape",8000),("Peach",9400),("Persimmon",7000),("Banana", 4000)]
cur.executemany("INSERT INTO items (name,price) VALUES(?,?)", data)
conn.commit()

# 4000-7000원 사이의 데이터 추출하기
# insert하는 것 처럼 ?에 들어갈 수치를 변수로 지정해놓고
# cursor.execute()로 쿼리문을 만들어준다.
cur = conn.cursor()
price_range = (4000, 7000)
cur.execute("SELECT * FROM items WHERE price >=? AND price <=?",price_range)

# cursor.fetchall()로 쿼리문의 결과에 대해 모두 출력 하게 한다.
fr_list = cur.fetchall()
for fr in fr_list:
    print(fr)