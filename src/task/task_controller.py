from fastapi import APIRouter
from . import task_service

from src.task.task_model import TaskResponse

task_router = APIRouter(prefix="/tasks",tags=["Tasks"])

@task_router.get("",response_model=TaskResponse)
def get_tasks():
    return task_service.get_tasks()