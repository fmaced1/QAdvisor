import redis, pickle, zlib, os

class RedisCache(object):
    def __init__(self):
        redis_host = os.getenv('REDIS_HOST')
        redis_port = os.getenv('REDIS_PORT')
        
        if redis_host == None and redis_port == None:
            redis_host = "localhost"
            redis_port = 6379

        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port)

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