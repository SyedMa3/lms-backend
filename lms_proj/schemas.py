from pydantic import BaseModel

class BookBase(BaseModel):
    title: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    timesIssued: int
    inv_id: int

    class Config:
        orm_mode = True