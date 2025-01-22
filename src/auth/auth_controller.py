from fastapi import APIRouter
from src.auth.auth_model import AuthResponse, LoginUserModel
from starlette import status
import os
from dotenv import load_dotenv
from src.auth.auth_service import create_jwt_token
from datetime import timedelta

load_dotenv()

auth_router = APIRouter(prefix="/auth",tags=["Auth"])

@auth_router.post("/login",response_model=AuthResponse,status_code=status.HTTP_200_OK)
def login(user_data:LoginUserModel):
    user = user_data.model_dump()
    jwt_token = create_jwt_token(user["email"],timedelta(minutes=10))
    # return AuthResponse(access_token=os.getenv("SECRET_ACCESS_KEY"),token_type="Bearer",user=user["email"])
    return AuthResponse(access_token=jwt_token,token_type="JWT",user=user["email"])