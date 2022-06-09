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

class StudentBase(BaseModel):
    rollNo: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    booksIssued: int

    class Config:
        orm_mode=True

class IssueBase(BaseModel):
    title: str
    issuedBy: int

class IssueCreate(IssueBase):
    pass

class Issue(IssueBase):
    id: int
    book_id: int

    class Config:
        orm_mode = True

class InventoryBase(BaseModel):
    title: str

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    id: int
    stock: int

    class Config:
        orm_mode: int