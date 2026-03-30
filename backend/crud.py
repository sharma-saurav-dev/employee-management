from typing import List, Optional
from sqlmodel import select, Session
from models import Employee


def get_employees(session: Session, skip: int = 0, limit: int = 100) -> List[Employee]:
    statement = select(Employee).offset(skip).limit(limit)
    return session.exec(statement).all()


def get_employee(session: Session, employee_id: int) -> Optional[Employee]:
    return session.get(Employee, employee_id)


def create_employee(session: Session, employee: Employee) -> Employee:
    session.add(employee)
    session.commit()
    session.refresh(employee)
    return employee


def update_employee(session: Session, employee_id: int, employee_data: dict) -> Optional[Employee]:
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


def delete_employee(session: Session, employee_id: int) -> bool:
    employee = session.get(Employee, employee_id)
    if not employee:
        return False
    session.delete(employee)
    session.commit()
    return True
