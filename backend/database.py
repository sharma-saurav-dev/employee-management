from sqlmodel import create_engine, Session

SQLITE_FILE_NAME = "employee.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{SQLITE_FILE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
