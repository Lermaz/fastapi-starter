from fastapi import FastAPI
from src.auth.router import router as auth_router
from src.posts.router import router as posts_router

app = FastAPI(title="FastAPI Best Practices Skeleton")

# Routers would be included here, e.g.:
# from .auth.router import router as auth_router
# app.include_router(auth_router) 

app.include_router(auth_router)
app.include_router(posts_router) 