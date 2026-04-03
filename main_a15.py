from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

enrollments = []

class Student(BaseModel):
    name: str
    student_id: str

class Course(BaseModel):
    name: str
    credits: int

class Enrollment(BaseModel):
    student: Student
    courses: List[Course]
    scholarship_rate: float = 0.0

@app.post("/enroll")
def enroll(data: Enrollment):
    credits = sum(c.credits for c in data.courses)
    tuition = credits * 300
    final = tuition - (tuition * data.scholarship_rate)

    enrollments.append(data)

    return {
        "total_credits": credits,
        "tuition_due": final,
        "data": data
    }

@app.get("/enrollments")
def get_all():
    return enrollments
