from fastapi import APIRouter
from starlette import status
from typing import Any
from . import task_service
from src.task.task_model import CreateTaskRequest, TaskResponse

task_router = APIRouter(prefix="/tasks",tags=["Tasks"])

@task_router.get("",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def get_tasks():
    return task_service.get_tasks()

@task_router.get("/{id}",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def get_task(id:str):
    return task_service.get_task(id)

@task_router.post("",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def create_task(task_data:CreateTaskRequest):
    return task_service.create_task(task_data)

@task_router.patch("/{id}",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def update_task(id:str,task_data:dict):
    return task_service.update_task(id,task_data)