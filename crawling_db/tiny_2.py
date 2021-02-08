# 데이터베이스 연결하기
from tinydb import TinyDB, Query

filepath = "./sql/test-tinydb.json"
db = TinyDB(filepath)

# 테이블 생성 / 추가하기
table = db.table('fruits1')

# 특정 데이터 추출하기
Item = Query()
res = table.search(Item.name == "Orange")
print('Orange is ', res[0]['price'])
