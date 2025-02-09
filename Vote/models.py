from sqlalchemy import Column, Integer, String, Boolean, func, ForeignKey, Enum, DateTime, Text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .schemas import NameEnum
 
class vote(Base):
    __tablename__ = "vote"

    id = Column(Integer, primary_key = True, nullable = False)
    Leader = Column(String, nullable = False)
    Name_of_Voter = Column(String, nullable = False)
    Reason = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone = True),server_default = func.now() ,nullable = False)
    owner_id = Column(Integer, ForeignKey("user.id" , ondelete = "CASCADE"),nullable = False) 
    owner = relationship("user")
    

class user(Base):
    __tablename__= "user"

    id = Column(Integer, primary_key = True, nullable = False)
    email = Column(String, unique = True, nullable = False )
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone = True),server_default=func.now(),onupdate = func.now() ,nullable = False)
    otp  =  Column(String)


class PatientORM(Base):
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    appointments = relationship("AppointmentORM", back_populates="patient")
    

class DoctorORM(Base):
    __tablename__ = "doctors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    appointments = relationship("AppointmentORM", back_populates="doctor")
   

class AppointmentORM(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    summary = Column(Text)
    
    patient = relationship("PatientORM", back_populates="appointments")
    doctor = relationship("DoctorORM", back_populates="appointments")