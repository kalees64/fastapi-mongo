from typing import Any

from pydantic import BaseModel


class TaskResponse(BaseModel):
    data:Any