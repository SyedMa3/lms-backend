from sqlalchemy.orm import Session

from . import models, schemas

def add_book(session: Session, book: schemas.BookCreate):
    new_inventory = add_inventory(session, book.title)
    new_book = models.Book(title = book.title, inv_id = new_inventory.id)
    session.add(new_book)

    return


def add_student(session: Session, student: schemas.StudentCreate):
    new_student = models.Student(rollNo = student.rollNo)
    session.add(new_student)
    session.commit()
    
    return

def add_inventory(session: Session, title):
    new_inventory = models.Inventory(title = title)
    session.add(new_inventory)
    session.commit()
    session.refresh(new_inventory)

    return new_inventory

