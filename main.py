from fastapi import FastAPI
from app.routes.users_routes import router as user_router
from app.core.logs import setup_logging

app = FastAPI(title="CRUD Cursos API")
# Configuração do logging
setup_logging()
app.include_router(user_router, prefix="/api/v1/users")
