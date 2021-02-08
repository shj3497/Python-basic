from tinydb import TinyDB, Query

filepath = "./sql/test-tinydb.json"
db = TinyDB(filepath)

# 테이블 생성 / 추가하기
table = db.table('fruits1')
#print(table.all())
"""
print(table.all())
[{'name': 'banana', 'price': 6000}, {'name': 'Orange', 'price': 12000}, {'name': 'mango', 'price': 8400}]
"""
"""
.json 파일의 형태
{
    "fruits1" : 
            {
             "1": {"name": "banana", "price": 6000}, 
             "2": {"name": "Orange", "price": 12000}, 
             "3": {"name": "mango", "price": 8400}
            }
}
"""
# 특정 데이터 추출하기
Item = Query()

# 8000원 이상인것 추출하기
print("### 8,000원 이상! ###")
result = table.search(Item.price >= 8000)
#print(result)
"""
print(result)
[{'name': 'Orange', 'price': 12000}, {'name': 'mango', 'price': 8400}]
"""
for it in result:
    print("-", it['name'])