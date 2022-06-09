from sqlalchemy import update
from sqlalchemy.orm import Session

from . import models, schemas

def add_book(session: Session, book: schemas.BookCreate):
    new_inventory = add_inventory(session, book.title)
    new_book = models.Book(title = book.title, inv_id = new_inventory.id)
    session.add(new_book)
    session.commit()
    session.refresh(new_book)

    return new_book


def add_inventory(session: Session, title):
    new_inventory = models.Inventory(title = title)
    session.add(new_inventory)
    session.commit()
    session.refresh(new_inventory)

    return new_inventory

def update_inventory(session: Session, title: str, new_stock: int):
    session.query(models.Inventory).filter(models.Inventory.title == title).\
        update({models.Inventory.stock: new_stock})
    session.commit()
    return

def add_student(session: Session, student: schemas.StudentCreate):
    new_student = models.Student(rollNo = student.rollNo)
    session.add(new_student)
    session.commit()
    session.refresh(new_student)

    return new_student

def issue_book(session: Session, issue: schemas.IssueCreate):
    current_book = session.query(models.Book).filter(models.Book.title == issue.title).first()
    current_student = session.query(models.Student).\
        filter(models.Student.rollNo == issue.issuedBy).first()
    current_book.timesIssued += 1
    current_student.booksIssued += 1
    # print(current_book)
    new_issue = models.Issue(title = issue.title,\
         book_id = current_book.id, issuedBy = current_student.rollNo)

    session.add(new_issue)
    session.commit()
    
    return