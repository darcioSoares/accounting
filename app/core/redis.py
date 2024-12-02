import redis
import os
import logging



REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Conexão com o Redis
# decode_responses=True: Faz o Redis retornar strings em vez de bytes
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


def redis_connection():
    try:
        redis_client.ping()
        logging.info("Conexão com Redis bem-sucedida!")
    except redis.ConnectionError as e:
        logging.error(f"Não foi possível conectar ao Redis: {e}")
        raise

#use
# from config_redis import redis_client

# # Salvar um valor no Redis
# redis_client.set("chave", "valor")

# # Buscar o valor salvo
# valor = redis_client.get("chave")
# print(f"O valor de 'chave' é: {valor}")


# # Salvar um valor com tempo de vida de 10 segundos
# redis_client.setex("chave_temporaria", 10, "valor")