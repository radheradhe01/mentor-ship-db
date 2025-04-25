from fastapi import FastAPI
from app.routers import users

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
# Add other routers as you implement them
