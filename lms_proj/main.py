from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from tables import Base

from fastapi import FastAPI

engine = create_engine('mysql://root:password@localhost/lms', echo=True)
Base.metadata.create_all(engine)


app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}