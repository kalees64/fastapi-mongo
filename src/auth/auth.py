from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from fastapi import HTTPException,Depends
from dotenv import load_dotenv
import os
from starlette import status
from typing import Annotated


load_dotenv()

bearer_auth = HTTPBearer()

def verify_bearer_token(bearer_token:Annotated[HTTPAuthorizationCredentials,Depends(bearer_auth)]):
    if bearer_token.scheme == "Bearer" and bearer_token.credentials == os.getenv("SECRET_ACCESS_KEY"):
        return {"token":bearer_token.credentials }
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Bearer Token")