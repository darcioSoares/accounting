from fastapi import FastAPI
from app.routes.users_routes import router as user_router

app = FastAPI(title="CRUD Cursos API")
app.include_router(user_router, prefix="/api/v1/users")
