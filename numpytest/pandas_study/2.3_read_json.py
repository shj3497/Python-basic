import pandas

df = pandas.read_json("./data/read_json_sample.json")
print(df)
print("\n")
print(df.index)
# 최초의 키값이 각 열 인덱스를 나타내고,
# 키값에 해당하는 value들을 열로 나타낸다.