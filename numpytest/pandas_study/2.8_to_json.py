import pandas

data = {'name' : [ 'Jerry', 'Riah', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"],
        }

df = pandas.DataFrame(data)
df.set_index('name',inplace=True) # name열을 인덱스로 지정
print(df)

# to_json() 메소드를 사용하여 JSON파일로 내보내기.
df.to_json("./data/df_sample.json")
