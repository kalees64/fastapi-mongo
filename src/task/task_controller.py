from fastapi import APIRouter
from . import task_service
from src.task.task_model import TaskResponse, CreateTaskRequest

task_router = APIRouter(prefix="/tasks",tags=["Tasks"])

@task_router.get("/",response_model=TaskResponse)
def get_tasks():
    return task_service.get_tasks()

@task_router.get("/{id}")
def get_task(id:str):
    return task_service.get_task(id)

@task_router.post("/",response_model=TaskResponse)
def create_task(task_data:CreateTaskRequest):
    return task_service.create_task(task_data)
