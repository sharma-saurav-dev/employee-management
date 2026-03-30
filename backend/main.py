from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Session

from database import engine, get_session
from crud import get_employees, get_employee, create_employee, update_employee, delete_employee
from models import Employee

app = FastAPI(title="Employee Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.get("/employees", response_model=list[Employee])
def read_employees(*, session: Session = Depends(get_session), skip: int = 0, limit: int = 100):
    return get_employees(session=session, skip=skip, limit=limit)


@app.get("/employees/{employee_id}", response_model=Employee)
def read_employee(*, session: Session = Depends(get_session), employee_id: int):
    employee = get_employee(session=session, employee_id=employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.post("/employees", response_model=Employee, status_code=201)
def create_employee_endpoint(*, session: Session = Depends(get_session), employee: Employee):
    return create_employee(session=session, employee=employee)


@app.put("/employees/{employee_id}", response_model=Employee)
def update_employee_endpoint(*, session: Session = Depends(get_session), employee_id: int, employee: Employee):
    updated = update_employee(session=session, employee_id=employee_id, employee_data=employee.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated


@app.delete("/employees/{employee_id}")
def delete_employee_endpoint(*, session: Session = Depends(get_session), employee_id: int):
    success = delete_employee(session=session, employee_id=employee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"ok": True}
