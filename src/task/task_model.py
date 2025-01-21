from typing import Any, Optional
from datetime import datetime,timezone
from pydantic import BaseModel,Field,ValidationError


class TaskResponse(BaseModel):
    data:Any

class CreateTaskRequest(BaseModel):
    name:str
    description:Optional[str] = None