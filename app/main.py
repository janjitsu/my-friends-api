from fastapi import FastAPI, Depends
from app.routes import api
from app.core.friends import Friends

app = FastAPI()

app.include_router(api.router)
