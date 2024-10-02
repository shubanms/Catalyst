from fastapi import FastAPI

from src.routes import health, new_user, auth

app = FastAPI()

app.include_router(health.router, prefix="/health")
app.include_router(new_user.router, prefix="/new-user")
app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/user")
