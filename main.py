# from dataclasses import Field, field

from fastapi import FastAPI , Depends
import schema  
from random import randint
import psycopg  


from pathlib import Path
import models 
from sqlalchemy.orm import Session
from database import engine, get_db
from models import SampleEcom , User
import schema   

from routers import auth, sample_ecom, user


models.Base.metadata.create_all(bind=engine) 


app = FastAPI()



set = [
       {
           "name": "Item 1",
           "description": "This is item 1", 
           "rating": 4 ,  
           "id": 2
       }]


def find_id(id):
    for item in set:
        if item["id"] == id:
            return item
    return None
print()


app.include_router(sample_ecom.router)
app.include_router(user.router)
app.include_router(auth.router)

