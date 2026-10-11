from fastapi import FastAPI
from pydantic import BaseModel
from random import randint
import psycopg
from dotenv import load_dotenv
import os
from pathlib import Path

###############################
env_path = Path(__file__).resolve().parent / ".env"
print(env_path)

load_dotenv(env_path, override=True)
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


print("Host:", DB_HOST)
print("Port:", DB_PORT)
print("Database loaded:", bool(DB_NAME))
print("User:", DB_USER)
print("Password loaded:", bool(DB_PASSWORD))


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
def create_item(item: Item):
    cursor.execute("INSERT INTO sample_ecom (name, description, ratings) VALUES (%s, %s, %s) RETURNING * " , (item.name, item.description, item.ratings))
    result = cursor.fetchone()  # Fetch the result of the insert operation
    conn.commit()
    return {"message": "Item created successfully", "result": result}
      # Commit the transaction to save changes to the database
    # post_item = item.model_dump()

    # post_item["id"] = randint(1, 1000)
    # set.append(post_item)
    # return {"name": item.name, "description": item.description , "rating": item.rating , "id": post_item["id"]}

@app.get("/items/{id}")
def read_item(id: int):
    # print(type(id))
    item = find_id((int(id)))
    return {"data": item}

@app.delete("/items/{id}")
def delete_item(id: int):
    cursor.execute("DELETE FROM sample_ecom WHERE id = %s RETURNING *", (str(id),))
    result = cursor.fetchone()  # Fetch the result of the delete operation
    conn.commit()  # Commit the transaction to save changes to the database

    return {"message": "Item deleted successfully", "result": result}


