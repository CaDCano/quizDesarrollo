from sqlmodel import create_engine, Session, SQLModel
from fastapi import Depends

db_url = "sqlite:///./transportes.db"
engine = create_engine(db_url)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Depends(get_session)

def init_db():
    SQLModel.metadata.create_all(engine)
