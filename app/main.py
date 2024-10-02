from fastapi import FastAPI
from app.api.v1.endpoints import translation

app = FastAPI()

app.include_router(translation.router, prefix="/api/v1/translation")
