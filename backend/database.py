from sqlmodel import create_engine

SQLITE_FILE_NAME = "employee.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{SQLITE_FILE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
