from pydantic import BaseModel, EmailStr

class Item(BaseModel):
    name: str
    description: str  | None = None
    ratings: int | None = None

class Response(BaseModel):
    name: str
    description: str  | None = None
    ratings: int | None = None

    class Config:
        orm_model = True

class schemauser(BaseModel):
    email: EmailStr
    password: str

class emailresponse(BaseModel):
    email: EmailStr