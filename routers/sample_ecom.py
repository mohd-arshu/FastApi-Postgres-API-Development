from fastapi import FastAPI , Depends, APIRouter
from models import SampleEcom , User
import schema
from sqlalchemy.orm import Session
from database import get_db
import models
import psycopg 
import os
from dotenv import load_dotenv
import Oauth2

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)
load_dotenv()


##################################

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

######################################################################
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

@router.get("/")
def read_root():
    cursor.execute("SELECT * FROM sample_ecom") 
    sqlquery = cursor.fetchall()
    return {"data":sqlquery } # Replace with your actual table name

    # Replace with your actual table name

@router.post("/",response_model=schema.Responsenew)
def create_item(sample:schema.Item, db: Session = Depends(get_db), user_id: int=Depends(Oauth2.get_current_user) ):
    # print(**sample.model_dump())


    # cursor.execute("INSERT INTO sample_ecom (name, description, ratings) VALUES (%s, %s, %s) RETURNING * " , (item.name, item.description, item.ratings))
    # result = cursor.fetchone()  # Fetch the result of the insert operation
    # conn.commit()
    SammpleEcom = models.SampleEcom(**sample.model_dump())
    
    print(user_id)
    db.add(SammpleEcom)
    db.commit()
    db.refresh(SammpleEcom)

    return {"message": "Item created successfully", "result": SammpleEcom}
      # Commit the transaction to save changes to the database
    # post_item = item.model_dump()

    # post_item["id"] = randint(1, 1000)
    # set.append(post_item)
    # return {"name": item.name, "description": item.description , "rating": item.rating , "id": post_item["id"]}

@router.get("/{id}",response_model=schema.Response)
def read_item(id: int , db: Session = Depends(get_db)):
    post_item = db.query(models.SampleEcom).filter(models.SampleEcom.id == id).first()
    print(post_item)
    return post_item
    # print(type(id))

@router.delete("/{id}",response_model=schema.Response)
def delete_item(id: int , db: Session = Depends(get_db)):
    item = db.query(models.SampleEcom).filter(models.SampleEcom.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return item


@router.get("/sqlquery")
def test_sqlquery(db: Session = Depends(get_db)):
    # return {"Status"    : "Success" , "data": db.query(models.Sample_Ecom).all() }
    query = db.query(models.SampleEcom).all()
    return {"Status"    : "Success" , "data": query }
