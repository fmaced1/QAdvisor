import redis, pickle, zlib

class RedisCache(object):
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379)

    def set_value(self, _key, _value, expiration_seconds):
        """ Loads json object into redis

        Args:
            _key ([string]): [key must be string]
            _value ([json]): [Loads json compress with zlib and store into redis]
            expiration_seconds ([int]): [life time seconds limit for data]
        """
        self.redis_client.setex(_key, expiration_seconds, zlib.compress(pickle.dumps(_value)))

    def get_value(self, _key):
        """ Get content from values

        Args:
            _key ([string]): [get json content from redis]

        Returns:
            [dict]: [json content]
        """
        return pickle.loads(zlib.decompress(self.redis_client.get(_key)))