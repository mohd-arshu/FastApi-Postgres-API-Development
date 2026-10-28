

from fastapi import FastAPI , Depends, APIRouter
from models import User
import models
import schema
from sqlalchemy.orm import Session
from database import get_db
import utils

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/",response_model=schema.emailresponse)
def create_user(user: schema.schemauser, db: Session = Depends(get_db)):
    user.password = utils.password_hash(user.password)
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
