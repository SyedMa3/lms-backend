from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from lms_proj.models import Base

from fastapi import FastAPI

engine = create_engine('mysql://root:password@localhost/lms', echo=True)
Base.metadata.create_all(engine)


app = FastAPI()

@app.post('/book')
async def addBook():
    return {'message': 'Hello World'}