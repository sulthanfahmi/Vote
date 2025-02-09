from typing import List, Optional
from fastapi import  FastAPI,Response,status,HTTPException,Depends, APIRouter, BackgroundTasks

from sqlalchemy.orm import Session 
from ..import models,schemas , oauth2 ,database
from ..database import get_db, SessionLocal
from ..schemas import NameEnum
from typing import List



router = APIRouter(
    prefix = "/appointments",
    tags = ["Appointments"]
)


# Background task to generate appointment summary and send emails
def process_appointment(appointment_id: int, db: Session = Depends(database.get_db)):

    appointment = db.query(models.AppointmentORM).filter(models.AppointmentORM.id == appointment_id).first()
    if not appointment:
        return
    patient = appointment.patient
    doctor = appointment.doctor
    summary_report = f"Summary Report for Appointment ID {appointment_id}: {appointment.summary}"
  
    db.close()



@router.post("/",response_model = schemas.Appointment)
async def create_appointment(appointment: schemas.Appointment, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    db_appointment = models.AppointmentORM(
        patient_id=appointment.patient.id,
        doctor_id=appointment.doctor.id,
        summary=appointment.summary
    )
    # Add the newly created appointment to the database session
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)

     # Schedule background task after successful appointment creation
    background_tasks.add_task(process_appointment, appointment_id=db_appointment.id, db=db)  # Pass db session

    return {"message": "Appointment created successfully!"}