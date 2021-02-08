import pandas
import pyarrow
import redis

df = pandas.DataFrame({'A':[1,2,3]})
r = redis.Redis(host="localhost", port=6379, db=0)

context = pyarrow.default_serialization_context()
r.set("key", context.serialize(df).to_buffer().to_pybytes())

rr = context.deserialize(r.get("key"))
print(rr)