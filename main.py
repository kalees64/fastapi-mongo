from fastapi_cli.cli import dev
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from src.config import database

app = FastAPI(title="FastAPI + MongoDB",version="0.0.1")

class Response(BaseModel):
    data:str

@app.get("/",tags=["Default"])
def root():
    print(f'-- DB Name : {database}')
    return Response(data="API is running")

if __name__ == "__main__":
    # uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)
    dev(port=3000,host="127.0.0.1",reload=True,path=Path("main.py"))