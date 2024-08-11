import redis
import pickle
import zlib
import os

class RedisCache:
    def __init__(self):
        redis_host = os.getenv('REDIS_HOST', 'localhost')
        redis_port = os.getenv('REDIS_PORT', 6379)

        try:
            self.redis_client = redis.StrictRedis(host=redis_host, port=int(redis_port))
            self.redis_client.ping()
        except redis.ConnectionError as e:
            raise Exception(f"Unable to connect to Redis at host {redis_host} on port {redis_port}: {e}")

    def get_value(self, _key: str):
        """
        Retrieves and decompresses the value associated with the key in Redis.

        Args:
            _key (str): The key to retrieve the value.

        Returns:
            dict: The decompressed value stored in Redis.

        Raises:
            Exception: If the key is not found or an error occurs during decompression/deserialization.
        """
        try:
            compressed_data = self.redis_client.get(_key)
            if compressed_data is None:
                # raise KeyError(f"Key {_key} not found in Redis.")
                return None
            
            return pickle.loads(zlib.decompress(compressed_data))
        except (TypeError, zlib.error, pickle.UnpicklingError) as e:
            raise Exception(f"Error decompressing/deserializing data for key {_key}: {e}")

    def set_value(self, _key: str, _value, expiration_seconds: int):
        """
        Compresses and stores a value in Redis with a key and expiration time.

        Args:
            _key (str): The key to store the value.
            _value: The value to be stored (will be serialized and compressed).
            expiration_seconds (int): The expiration time in seconds.

        Raises:
            Exception: If an error occurs during serialization/compression.
        """
        try:
            compressed_data = zlib.compress(pickle.dumps(_value))
            self.redis_client.setex(_key, expiration_seconds, compressed_data)
        except (TypeError, zlib.error, pickle.PicklingError) as e:
            raise Exception(f"Error compressing/serializing data for key {_key}: {e}")