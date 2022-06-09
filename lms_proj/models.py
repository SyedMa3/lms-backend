"""
    Models for creating the tables
"""
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), unique=True, index=True)
    timesIssued = Column(Integer, default = 0)
    inv_id = Column(Integer, ForeignKey('inventory.id'))

    issues = relationship('Issue', backref = 'book')

    def __repr__(self):
        return f'ID - {self.id}, Title - {self.title}, No. of Times Issued - {self.timesIssued}'


class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), unique=True, index=True)
    stock = Column(Integer, default=1)
    
    books = relationship('Book', backref = 'inventory')

    def __repr__(self):
        return f'ID - {self.id}, Title - {self.title}, Stock - {self.stock}'

class Student(Base):
    __tablename__ = 'student'

    rollNo = Column(Integer, primary_key=True, index=True)
    booksIssued = Column(Integer, default=0)

    issues = relationship('Issue', backref = 'student')

    def __repr__(self):
        return f'Roll No - {self.rollNo}, No. of Books Issued Currently - {self.booksIssued}'

class Issue(Base):
    __tablename__ = 'issue'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30))
    book_id = Column(Integer, ForeignKey('book.id'))
    issuedBy = Column(Integer, ForeignKey('student.rollNo'))

    def __repr__(self):
        return f'ID - {self.id}, Title - {self.title}, Issued By - {self.issuedBy}' 