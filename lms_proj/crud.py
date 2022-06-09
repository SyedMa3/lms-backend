"""
    Functions for the features described in PDF
"""
from sqlalchemy import update, desc
from sqlalchemy.orm import Session
from fastapi import HTTPException

from . import models, schemas

def add_book(session: Session, book: schemas.BookCreate):
    """
    Adds a book entry
    """
    new_inventory = add_inventory(session, book.title)
    new_book = models.Book(title = book.title, inv_id = new_inventory.id)
    session.add(new_book)
    session.commit()
    session.refresh(new_book)

    return new_book


def add_inventory(session: Session, title):
    """
    Adds the book to the inventory table
    """
    new_inventory = models.Inventory(title = title)
    session.add(new_inventory)
    session.commit()
    session.refresh(new_inventory)

    return new_inventory

def update_inventory(session: Session, title: str, new_stock: int):
    """
    To Update the stock of the given book
    """
    session.query(models.Inventory).filter(models.Inventory.title == title).\
        update({models.Inventory.stock: new_stock})
    session.commit()
    return

def add_student(session: Session, student: schemas.StudentCreate):
    """
    To add a student to the database
    """
    new_student = models.Student(rollNo = student.rollNo)
    session.add(new_student)
    session.commit()
    session.refresh(new_student)

    return new_student

def issue_book(session: Session, issue: schemas.IssueCreate):
    """
    To issue a book by a given student
    """
    current_book = session.query(models.Book).filter(models.Book.title == issue.title).first()
    
    if current_book == None:
        raise HTTPException(status_code=404, detail="Book not found")

    current_student = session.query(models.Student).\
        filter(models.Student.rollNo == issue.issuedBy).first()

    if current_student == None:
        raise HTTPException(status_code=404, detail="Student not found")

    current_inventory = session.query(models.Inventory).\
        filter(models.Inventory.id == current_book.inv_id).first()

    if current_student.booksIssued == 3:
        raise HTTPException(status_code=404, detail="Student can only hold 3 books")

    if current_inventory.stock == 0:
        raise HTTPException(status_code=404, detail="This book is currently not available")

    current_inventory.stock -= 1
    current_book.timesIssued += 1
    current_student.booksIssued += 1
    
    new_issue = models.Issue(title = issue.title,\
         book_id = current_book.id, issuedBy = current_student.rollNo)

    session.add(new_issue)
    session.commit()
    session.refresh(new_issue)
    
    return new_issue

def return_book(session: Session, issue: schemas.IssueCreate):
    """
    To return a given book by a given student
    """
    current_book = session.query(models.Book).filter(models.Book.title == issue.title).first()
    
    if current_book == None:
        raise HTTPException(status_code=404, detail="Book not found")

    current_student = session.query(models.Student).\
        filter(models.Student.rollNo == issue.issuedBy).first()

    if current_student == None:
        raise HTTPException(status_code=404, detail="Student not found")

    current_inventory = session.query(models.Inventory).\
        filter(models.Inventory.id == current_book.inv_id).first()

    current_issue = session.query(models.Issue).\
        filter(models.Issue.issuedBy == issue.issuedBy and models.Issue.title == issue.title).\
            first()
    
    if current_issue == None:
        raise HTTPException(status_code=404, detail="The student has not issued this book")
    
    current_inventory.stock += 1
    current_student.booksIssued -= 1
    

    session.delete(current_issue)
    session.commit()

    return

def popular_books(session: Session):
    """
    To display the top 5 issued books
    """

    books = session.query(models.Book).order_by(desc(models.Book.timesIssued)).limit(5).all()

    return books
