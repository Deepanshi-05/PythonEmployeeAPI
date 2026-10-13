from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Employee(BaseModel):
    name: str
    department: str


@app.get("/")
def home():
    return {"message": "My first Python API is working!"}


@app.get("/employees")
def get_employees():
    employees = [
        {
            "id": 1,
            "name": "Aarav",
            "department": "IT"
        },
        {
            "id": 2,
            "name": "Priya",
            "department": "HR"
        }
    ]

    return employees


@app.post("/employees")
def create_employee(employee: Employee):
    return {
        "message": "Employee created successfully",
        "employee": employee
    }
