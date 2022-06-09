from email.policy import default
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

engine = create_engine('mysql://root:password@localhost/lms', echo=True)

Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable = False, ForeignKey = 'inventory.title')
    timesIssued = Column(Integer, default = 0)

    inInventory = relationship('Inventory', backref = 'book')
    issues = relationship('Issue', backref = 'book')


class Inventory(Base):
    __tablename__ = 'inventory'

    title = Column(String, primary_key=True)
    stock = Column(Integer, default=1)

class Student(Base):
    __tablename__ = 'student'

    rollNo = Column(Integer, primary_key=True)
    booksIssued = Column(Integer, default=0)

    issues = relationship('Issue', backref = 'student')

class Issue(Base):
    __tablename__ = 'issue'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable = False, ForeignKey = 'book.title')
    issuedBy = Column(Integer, ForeignKey='student.rollNo')