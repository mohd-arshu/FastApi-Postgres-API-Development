from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from database import get_db
import models
from routers import user
import schema
import utils
import Oauth2
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(tags=["Authentication"],prefix="/auth") 

@router.post("/login")
def login(schema: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Implement your login logic here
    

    user = db.query(models.User).filter(models.User.email == schema.username).first()

    if not user:
        return {"error": "Invalid email or password"}

    if not utils.verify(schema.password, user.password):
        return {"error": "Invalid email or password"}

    verification_token = Oauth2.create_access_token(data={"user_id": user.id})

    return {"token": verification_token}  # Replace with your actual token generation logic

# return {"message": "token"}
