from tinydb import TinyDB, Query

###
# tinydb.purge() 사용 금지
# tinydb.remove(query) Remove all documents matching the query
###
# db에 연결하기
filepath = "./sql/test-tinydb.json"
db = TinyDB(filepath)

# 기존의 테이블이 있다면 제거하기
# db.purge_table('fruits1')

# 테이블 생성 / 추가하기
# tinydb는 일반적인 query문이 아니네..
table = db.table('fruits1')

# 테이블에 데이터 추가하기
table.insert({'name':'banana','price':6000})
table.insert({'name':'Orange','price':12000})
table.insert({'name':'mango','price':8400})

# 모든 데이터 추출하기
print(table.all())

# 특정 데이터 추출하기
# 데이터를 추출한다. >> select한다는 소리인데 
Item = Query()
# table >> 16행 db.table('fruits1')로 만들어준 테이블 사용
# table.search( )
# Item.name >> ? : name이라는 키값을 모조리 검색하는건가..? >> 맞는듯
res = table.search(Item.name == 'Orange')
print('Orange is ', res[0]['price'])

# 가격이 8000원 이상인 것 추출하기
print('### 8000원 이상 과일 ###')
res = table.search(Item.price >= 8000)
for it in res:
    print("-", it['name'])

# 계속 실행하면 table.insert로 데이터가 계속 들어감