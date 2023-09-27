from fastapi import FastAPI
from router import estatic

app = FastAPI()

app.include_router(estatic)
