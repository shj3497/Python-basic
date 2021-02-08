from tinydb import TinyDB, Query

filePath = "./sql/db.json"
db = TinyDB(filePath)
# 테이블 명을 선언해주지 않고 json파일을 만든다?
# >> 파일자체를 하나의 테이블만 존재하도록 하겠다는건가..
# >> NO 테이블명을 지정하지 않으면 '_default' 라는 이름으로 테이블이 생성된다.
# tdb = TinyDB(filePath)
# db = tdb.table("tiny_4")
User = Query()

# 흠..? tb = db.table(테이블명)
# tb.insert()일텐데..?
def insert_user():
    db.insert({'name':'John', 'age':22})
    db.insert({'name':'Max', 'age':25})
    db.insert({'name':'Sarah', 'age': 21, 'city':'New York'})

def search_user():
    # where city = 'New York' 인
    results = db.search(User.city == 'New York')
    for res in results:
        print(res['city'])
    results = db.search(User.age > 21)
    for res in results:
        # 딕셔너리를 뽑아내겠다는 것
        # 결과는 배열(list)로 출력된다.
        print(res)

def update_user():
    # 얘는 .update()라는 함수를 사용하여 업데이트 해줌
    db.update({'age':26}, User.name == 'Max')
    # .json 파일을 읽겠다
    for item in db:
        print(item)

    """
    # 'or' 위 또는 아래코드로 update실행 
    results = db.search(User.name == 'Max')
    # 얘는 특정 컬럼을 지정해서 특정 키값을 지정해서 value를 바꾸는 행위
    for res in results:
        res['age'] = 27
    # .write_back(results) : 결과를 재 업로드 한다. >> 다시쓴다
    db.write_back(results)
    """

def delete_user():
    db.remove(User.name == 'John')
    # .remove() 함수를 이용해서 지운다.
    # db.purge() # remove all

def update_by_document_id():
    # db.remove(doc_ids=[2])
    # this will not create doc_id=2, but the next highest number
    # db.insert({'name': 'Jason', 'age': 40})
    item = db.get(doc_id=3)
    print(item)
    print(item.doc_id)

    # 흠....
    db.update({'city':'Boston'}, doc_ids=[1,2])
    #db.remove(doc_ids=[1, 2])

### TEST ###
### 주석 풀어서 사용! ###
#insert_user()
#search_user()
#update_user()
#delete_user()
#update_by_document_id()
print(db.all())