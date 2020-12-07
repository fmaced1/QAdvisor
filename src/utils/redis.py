import redis, pickle, zlib

redis_client = redis.StrictRedis(host='localhost', port=6379)

class CacheStore:
    def set_redis(ticker, content, expiration_seconds):
        redis_client.setex(ticker, expiration_seconds, zlib.compress(pickle.dumps(content)))

    def get_redis(ticker):
        return pickle.loads(zlib.decompress(redis_client.get(ticker)))