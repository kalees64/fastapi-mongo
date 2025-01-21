from fastapi import APIRouter,Depends
from starlette import status
from src.auth.auth_service import verify_bearer_token
from . import task_service
from src.task.task_model import CreateTaskRequest, TaskResponse, UpdateTaskRequest
from typing import Annotated

task_router = APIRouter(prefix="/tasks",tags=["Tasks"],dependencies=[Depends(verify_bearer_token)])
# guard = Annotated[dict,Depends(verify_bearer_token)]


@task_router.get("",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def get_tasks():
    return task_service.get_tasks()

@task_router.get("/{id}",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def get_task(id:str):
    return task_service.get_task(id)

@task_router.post("",response_model=TaskResponse,status_code=status.HTTP_201_CREATED)
def create_task(task_data:CreateTaskRequest):
    return task_service.create_task(task_data)

@task_router.patch("/{id}",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def update_task(id:str,task_data:UpdateTaskRequest):
    return task_service.update_task(id,task_data)

@task_router.delete("/{id}",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def delete_task(id:str):
    return task_service.delete_task(id)