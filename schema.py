from typing import Optional

from pydantic import BaseModel, EmailStr

class Item(BaseModel):
    name: str
    description: str  | None = None
    ratings: int | None = None

class Response(BaseModel):
    id: int
    name: str
    description: str  | None = None
    ratings: int | None = None

    class Config:
        orm_model = True

class Responsenew(BaseModel):
    message :str
    result: Response

class schemauser(BaseModel):
    email: EmailStr
    password: str

class emailresponse(BaseModel):
    email: EmailStr

class Userlogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] | None = None