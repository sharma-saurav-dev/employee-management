from typing import Optional
from sqlmodel import SQLModel, Field

class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str = Field(index=True)
    position: str
    salary: float
