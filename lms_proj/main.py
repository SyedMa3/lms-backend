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