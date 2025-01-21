from pydantic import BaseModel,EmailStr

class LoginUserModel(BaseModel):
    email:EmailStr
    password:str
    
class AuthResponse(BaseModel):
    access_token:str
    token_type:str = "JWT / Bearer"
    user:EmailStr
    