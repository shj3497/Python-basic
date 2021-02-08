import sqlite3

dbpath = "./sql/test.sqlite"
conn = sqlite3.connect(dbpath)

cur = conn.cursor()
# executescript() : 세미콜론으로 구분된 연속된 SQL문장을 수행한다.
# sqlite_1.py에서 Create와 Insert를 따로따로 해줬는데
# executescript로 한꺼번에 해줬다.
cur.executescript("""
                    /* items 테이블이 이미 있다면 제거하기 */
                    DROP TABLE IF EXISTS items;
                    /* 테이블 생성하기 */
                    CREATE TABLE items(
                        item_id INTEGER PRIMARY KEY,
                        name TEXT UNIQUE,
                        price INTEGER
                    );
                    /* 데이터 넣기 */
                    INSERT INTO items(name, price)VALUES('Apple', 800);
                    INSERT INTO items(name, price)VALUES('Orange', 780);  
                    INSERT INTO items(name, price)VALUES('Banana', 430);
                    """)
# 위의 조작을 데이터베이스에 반영하기
conn.commit()
# 여기까지의 connection을 commit한다는 의미인듯?

# 새로 커서를 호출
# 데이터 추출하기
cur = conn.cursor()
# execute() 쿼리문 실행
cur.execute("SELECT item_id,name,price FROM items")
# .fetchall() : 쿼리문의 결과를 모두 출력해줌
item_list = cur.fetchall()

# 출력하기
for it in item_list:
    print(it)

