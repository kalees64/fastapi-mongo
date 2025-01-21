from src.config.database import tasks_collection
from src.task.task_model import CreateTaskRequest, TaskResponse, UpdateTaskRequest
from bson import ObjectId
from fastapi import HTTPException
from starlette import status


def get_tasks():
    tasks = list(tasks_collection.find())
    # return {"data":[{**task,"id":str(task["_id"])} for task in tasks]}
    return TaskResponse(data=[{**task,"id":str(task["_id"])} for task in tasks])

def get_task(id:str):
    task = tasks_collection.find_one({"_id":ObjectId(id)})
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    # return {"data":{**task,"id":str(task["_id"])}}
    return TaskResponse(data={**task,"id":str(task["_id"])})

def create_task(task_data:CreateTaskRequest):
    new_task = tasks_collection.insert_one(task_data.model_dump())
    created_task = tasks_collection.find_one({"_id":new_task.inserted_id})
    # return {"data":{**created_task,"id":str(created_task["_id"])}}
    return TaskResponse(data={**created_task,"id":str(created_task["_id"])})

def update_task(id:str,task_data:UpdateTaskRequest):
    update_task_data = task_data.model_dump(exclude_unset=True)
    if len(update_task_data.keys()) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="No valid data to update")
    updated_task = tasks_collection.find_one_and_update({"_id":ObjectId(id)},{"$set":update_task_data},return_document=True)
    if not updated_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    # return {"data":{**updated_task,"id":str(updated_task["_id"])}}
    return TaskResponse(data={**updated_task,"id":str(updated_task["_id"])})

def delete_task(id:str):
    deleted_task = tasks_collection.find_one_and_delete({"_id":ObjectId(id)})
    if not delete_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    # return {"data":{**deleted_task,"id":str(deleted_task["_id"])}}
    return TaskResponse(data={**deleted_task,"id":str(deleted_task["_id"])})