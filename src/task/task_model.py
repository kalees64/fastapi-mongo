from typing import Any, Optional
from datetime import datetime,timezone
from pydantic import BaseModel,Field,ValidationError


class CreateTaskRequest(BaseModel):
    name:str
    description:Optional[str] = None
    


class TaskResponseModel(BaseModel):
    id:str
    name:str
    description:Optional[str] = None
    
class TaskResponse(BaseModel):
    data:TaskResponseModel | list[TaskResponseModel]
    
