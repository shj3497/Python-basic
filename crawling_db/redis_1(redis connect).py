import redis

# Ip주소와 port번호에 따른 커넥트
def connect_redis():
    try:
        # conn = redis.StrictRedis(host='localhost', port=6379, db=redis_info['db'])
        conn = redis.StrictRedis(host='localhost', port=6379)

    except Exception as e:
        print("DB connection error : ",e)
    return conn


def info_redis():
    conn = connect_redis()
    result = conn.info(section='memory')
    print(result)

info_redis()