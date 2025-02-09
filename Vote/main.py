from typing import Optional, List
from fastapi import  FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2 
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session 
from .import models, schemas, utils
from .database import engine,get_db
from .routers import user,auth,voter,appointments



models.Base.metadata.create_all(bind=engine) 

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host = "localhost" ,database = "Voter" ,user = "postgres",
                            password = "Welcome@123", cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("The Database was connected succesfully")
        break

    except Exception as error:
        print("The Database connection failed")
        print("Error", error)


app.include_router(voter.router)
app.include_router(user.router)
app.include_router(auth.routher)
app.include_router(appointments.router)