# from dataclasses import Field, field

from fastapi import FastAPI , Depends
import schema  
from random import randint
import psycopg
from dotenv import load_dotenv
import os
from pathlib import Path
import models 
from sqlalchemy.orm import Session
from database import engine, get_db
from models import SampleEcom , User
import schema

from routers import sample_ecom, user



models.Base.metadata.create_all(bind=engine) 


load_dotenv()


##################################

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


try:
    conn = psycopg.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()
    print("Connected to the database successfully!")
except Exception as e:
    print("Error connecting to the database:", e)

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