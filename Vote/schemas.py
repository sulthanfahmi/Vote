from pydantic import BaseModel,EmailStr, Field
from datetime import datetime 
from typing import Optional
from enum import Enum
from fastapi import Query

class NameEnum(str,Enum):
    OPTION1 = "Virat"
    OPTION2 = "Dhoni"
    OPTION3 = "Rohit"
    OPTION4 = "Raina"
    OPTION5 = "Faf"
    OPTION6 = "Maxwell"
    OPTION7 = "Smith"

class PostBase(BaseModel):
    
    Name_of_Voter : str
    Reason : str
    
    

class CreatePost(PostBase):
    pass

class display(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime

   
class Config:
     orm_mode = True

class Post(PostBase):
        id : int
        Leader : str
        created_at : datetime
        owner_id : int
        owner : display
        
class Config:
    orm_mode = True

# For the table name user

class usercreate(BaseModel):
    email : EmailStr
    password : str

class updateUser(usercreate):
     pass


class User_Login(BaseModel):
     email : EmailStr
     password : str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
     id : Optional[int]  = None
    

class user(BaseModel):
     email : EmailStr

class VerifyEmail(BaseModel):
     email : str
     otp: str
     
# For Back ground task in fastapi

class Patient(BaseModel):
    id: int
    name: str
    email: str
    
class Doctor(BaseModel):
    id: int
    name: str
    email: str
    

class Appointment(BaseModel):
    id: int
    patient: Patient
    doctor: Doctor
    summary: str
