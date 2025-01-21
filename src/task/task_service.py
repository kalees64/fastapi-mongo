from src.config.database import tasks_collection
from src.task.task_model import CreateTaskRequest,TaskResponse
from bson import ObjectId
from fastapi import HTTPException
from starlette import status


def get_tasks():
    tasks = list(tasks_collection.find())
    return {"data":[{**task,"_id":str(task["_id"])} for task in tasks]}

def get_task(id:str):
    task = tasks_collection.find_one({"_id":ObjectId(id)})
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    return TaskResponse(data={**task,"_id":str(task["_id"])})

def create_task(task_data:CreateTaskRequest):
    new_task = tasks_collection.insert_one(task_data.model_dump())
    created_task = tasks_collection.find_one({"_id":new_task.inserted_id})
    return {"data":{**created_task,"_id":str(created_task["_id"])}}