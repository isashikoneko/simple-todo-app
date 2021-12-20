from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def getAll():
    return {'message' : "Hello world"}


