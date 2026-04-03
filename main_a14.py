from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

appointments = []

class Patient(BaseModel):
    name: str
    age: int

class Treatment(BaseModel):
    name: str
    cost: float

class Appointment(BaseModel):
    patient: Patient
    treatments: List[Treatment]
    insurance_coverage: float = 0.0

@app.post("/book-appointment")
def book_appointment(data: Appointment):
    total = sum(t.cost for t in data.treatments)
    final = total - (total * data.insurance_coverage)

    appointments.append(data)

    return {
        "total_to_pay": final,
        "data": data
    }

@app.get("/appointments")
def get_data():
    return appointments
