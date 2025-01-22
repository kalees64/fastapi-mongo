import os
import dotenv
from fastapi_cli.cli import dev
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from src.config import database
from src.task.task_controller import task_router
from src.auth.auth_controller import auth_router

dotenv.load_dotenv()

app = FastAPI(title="FastAPI + MongoDB",version="0.0.1")


class Response(BaseModel):
    data:str

@app.get("/",tags=["Default"],response_model=Response)
def root():
    print(f'-- DB Name : {database}')
    return Response(data="API is running")

app.include_router(auth_router)
app.include_router(task_router)



# if __name__ == "__main__":
#     # uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)
#     dev(port=3000,host="127.0.0.1",reload=True,path=Path("main.py"))