import redis

redis_conn = redis.Redis(host='redis-17956.crce207.sa-east-1-2.ec2.redns.redis-cloud.com',
    port=17956,
    decode_responses=True,
    username="default",
    password="hFCZsrvnUiJ2IgRlxjQowvzj3pnGGv14",)
# para insert e update
redis_conn.set("chave_1", "trocando_o_meu_valor")

# select
meu_valor = redis_conn.get("chave_1").encode("utf-8")

# delete
redis_conn.delete("chave_1")

print(meu_valor)
