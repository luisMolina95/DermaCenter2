import os
from fastapi import FastAPI
from .database import inspector
app = FastAPI()

@app.get("/",tags=['ROOT'])
async def root() -> dict:
    return {"Ping": "Pong", "extra": os.environ.get('APP_TCP_PORT'), "tables": "{}".format(inspector.get_table_names())}