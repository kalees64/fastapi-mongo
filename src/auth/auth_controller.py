from fastapi import APIRouter
from src.auth.auth_model import AuthResponse, LoginUserModel
from starlette import status
import os
from dotenv import load_dotenv

load_dotenv()

auth_router = APIRouter(prefix="/auth",tags=["Auth"])

@auth_router.post("/login",response_model=AuthResponse,status_code=status.HTTP_200_OK)
def login(user_data:LoginUserModel):
    user = user_data.model_dump()
    return AuthResponse(access_token=os.getenv("SECRET_ACCESS_KEY"),token_type="Bearer",user=user["email"])