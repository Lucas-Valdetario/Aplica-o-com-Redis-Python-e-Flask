from redis import Redis

class RedisConnectionHandler:
    def __init__(self) -> None:
        self.__redis_conn = None

    def connect(self) -> Redis:
        redis_conn = Redis(host='redis-17956.crce207.sa-east-1-2.ec2.redns.redis-cloud.com',
        port=17956,
        decode_responses=True,
        username="default",
        password="hFCZsrvnUiJ2IgRlxjQowvzj3pnGGv14"
        )
        self.__redis_conn = redis_conn
        return redis_conn

    def get_connection(self) -> Redis:
        return self.__redis_conn