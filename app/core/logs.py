import logging
import os
from datetime import datetime

# Diretório para salvar os logs
LOG_DIR = os.path.join(os.path.dirname(__file__), "../../storage/logs")
os.makedirs(LOG_DIR, exist_ok=True)  # Cria o diretório, se não existir

# Nome do arquivo de log com data dinâmica
log_file = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log")

# Configuração do logger
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  # Nível mínimo do log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(levelname)s - %(message)s",  # Formato do log
        handlers=[
            logging.FileHandler(log_file),  # Salva no arquivo
            logging.StreamHandler()         # Também exibe no console
        ]
    )

logging.getLogger("sqlalchemy.engine").setLevel(logging.ERROR)

# from config_redis import redis_client

# # Salvar um valor no Redis
# redis_client.set("chave", "valor")

# # Buscar o valor salvo
# valor = redis_client.get("chave")
# print(f"O valor de 'chave' é: {valor}")