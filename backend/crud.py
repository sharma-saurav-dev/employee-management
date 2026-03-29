from typing import List, Optional
from sqlmodel import Session, select
from database import engine
from models import Employee


def get_employees(skip: int = 0, limit: int = 100) -> List[Employee]:
    with Session(engine) as session:
        statement = select(Employee).offset(skip).limit(limit)
        return session.exec(statement).all()


def get_employee(employee_id: int) -> Optional[Employee]:
    with Session(engine) as session:
        return session.get(Employee, employee_id)


def create_employee(employee: Employee) -> Employee:
    with Session(engine) as session:
        session.add(employee)
        session.commit()
        session.refresh(employee)
        return employee


def update_employee(employee_id: int, employee_data: dict) -> Optional[Employee]:
    with Session(engine) as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            return None
        for key, value in employee_data.items():
            if value is not None and key != "id":
                setattr(employee, key, value)
        session.add(employee)
        session.commit()
        session.refresh(employee)
        return employee


def delete_employee(employee_id: int) -> bool:
    with Session(engine) as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            return False
        session.delete(employee)
        session.commit()
        return True
