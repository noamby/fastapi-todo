from dogpile.cache.region import CacheRegion  # type: ignore


class CacheClient(CacheRegion):
    """
    Wrapper for CacheRegion class by dogpile.cache
    https://dogpilecache.sqlalchemy.org/en/latest/index.html
    Used to configure the cache backend while initializing the client only once
    A few things to notice:
        Unlike redis-py, set method does not contain expiration time,
        to support expiration time the get method can accept expiration_time.
        and it will verify the expiration against the creation time and return NO_VALUE
        if expired
    """
    def __init__(self, host: str, port: int, password: str):
        super().__init__()
        redis_settings = {
            "host": host,
            "port": port,
            "password": password,
        }
        self.configure("dogpile.cache.redis", arguments=redis_settings)
