from fastapi import FastAPI , Depends
from pydantic import BaseModel
from random import randint
import psycopg
from dotenv import load_dotenv
import os
from pathlib import Path
import models 
from sqlalchemy.orm import Session
from database import engine, get_db
from models import SampleEcom
# import csv

models.Base.metadata.create_all(bind=engine) 
###############################

# with open("sample_ecom.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         item = SampleEcom(
#             name=row["name"],
#             description=row["description"],
#             ratings=int(row["ratings"])
#         )
#         with Session(engine) as session:
#             session.add(item)
#             session.commit()

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




class Item(BaseModel):
    name: str
    description: str  | None = None
    ratings: int | None = None

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

@app.get("/")
def read_root():
    cursor.execute("SELECT * FROM sample_ecom") 
    sqlquery = cursor.fetchall()
    return {"data":sqlquery } # Replace with your actual table name

    # Replace with your actual table name

@app.post("/items/")
def create_item(sample:Item, db: Session = Depends(get_db)):
    # print(**sample.model_dump())


    # cursor.execute("INSERT INTO sample_ecom (name, description, ratings) VALUES (%s, %s, %s) RETURNING * " , (item.name, item.description, item.ratings))
    # result = cursor.fetchone()  # Fetch the result of the insert operation
    # conn.commit()
    SammpleEcom = models.SampleEcom(**sample.model_dump())
    

    db.add(SammpleEcom)
    db.commit()
    db.refresh(SammpleEcom)

    return {"message": "Item created successfully", "result": SammpleEcom}
      # Commit the transaction to save changes to the database
    # post_item = item.model_dump()

    # post_item["id"] = randint(1, 1000)
    # set.append(post_item)
    # return {"name": item.name, "description": item.description , "rating": item.rating , "id": post_item["id"]}

@app.get("/items/{id}")
def read_item(id: int , db: Session = Depends(get_db)):
    post_item = db.query(models.SampleEcom).filter(models.SampleEcom.id == id).first()
    print(post_item)
    return {"message": "Item retrieved successfully", "result": post_item}
    # print(type(id))

@app.delete("/items/{id}")
def delete_item(id: int , db: Session = Depends(get_db)):
    item = db.query(models.SampleEcom).filter(models.SampleEcom.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully", "result": item}


@app.get("/sqlquery")
def test_sqlquery(db: Session = Depends(get_db)):
    # return {"Status"    : "Success" , "data": db.query(models.Sample_Ecom).all() }
    query = db.query(models.SampleEcom).all()
    return {"Status"    : "Success" , "data": query }

    