from fastapi import FastAPI
from app.routes.users_routes import router as user_router
from app.core.logs import setup_logging
#from app.core.redis import redis_client , redis_connection
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do logging
setup_logging()

# Testando conexão com redis
#redis_connection()

app = FastAPI(title="CRUD Cursos API")

app.include_router(user_router, prefix="/api/v1/users")
