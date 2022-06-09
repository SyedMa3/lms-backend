from . import models, crud, schemas
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import create_session, engine

models.Base.metadata.create_all(engine)

app = FastAPI()

def get_session():
    session = create_session()
    try:
        yield session
    finally:
        session.close()

@app.post('/book/', response_model=schemas.Book)
async def add_book(book: schemas.BookCreate, session: Session = Depends(get_session)):
    return crud.add_book(session=session, book=book)

@app.post('/inventory/')
async def update_inventory(title: str, stock: int, session: Session = Depends(get_session)):
    crud.update_inventory(title=title, new_stock=stock, session=session)

    return

@app.post('/student/', response_model=schemas.Student)
async def add_student(student: schemas.StudentCreate, session: Session = Depends(get_session)):
    return crud.add_student(session=session, student=student)

@app.post('/issue/')
async def add_issue(issue: schemas.IssueCreate, session: Session = Depends(get_session)):
    return crud.issue_book(session=session, issue=issue)