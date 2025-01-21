from typing import Optional
from pydantic import BaseModel


class CreateTaskRequest(BaseModel):
    name:str
    description:Optional[str] = None
    
class UpdateTaskRequest(BaseModel):
    name:Optional[str] = None
    description:Optional[str] = None
    
class TaskResponseModel(BaseModel):
    id:str
    name:str
    description:Optional[str] = None
    
class TaskResponse(BaseModel):
    data:TaskResponseModel | list[TaskResponseModel]
    
