# Library Management - Backend
A small backend application of school library management system.
### Features:
- New books can be added.
- New Students can be added.
- Books inventory can be updated.
- Students can issue books and return them.
- A student can hold max 3 books.

---
## Getting Started

### Prerequisites
-   You need to have [Poetry](https://python-poetry.org/) installed on your system

-   ```
    poetry install
    ```

- The application currently uses MySQL. You can configure the database connection in [database.py](lms_proj/database.py) using `SQLALCHEMY_DATABASE_URL`

- Make sure you have created a database you mentioned above

-   Run this command to start the server. 
    ```
    poetry run uvicorn lms_proj.main:app --reload
    ```
    --reload is not used in production
    

---
## Structure of database:

It contains four tables.

- Book: (Contains the book entries)
    -   id - Unique ID
    -   title : Title of the book
    -   timesIssued : No. of times this book was issued
    -   inv_id : Foreign Key to Inventory referring to id

- Inventory: (To store the inventory of available books)
    -   id - Unique ID
    -   title : Title of the book
    -   stock : Available no. of books of this title

- Student: (To store the students added)
    -   rollNo - Roll No. of student(Also unique ID)
    -   booksIssued - No. of books currently held

- Issue: (To store the currently issued books)
    -   id - Unique ID
    -   title : Title of the book
    -   book_id : Foreign Key to Book table
    -   issuedBy : Foreign  Key to Student table

---
## Structure of Application:

-   [main.py](lms_proj/main.py) - Deals with routing,
-   [models.py](lms_proj/models.py) - To declare classes to create tables from ORM
-   [schemas.py](lms_proj/schemas.py) - Schemas of the models for Pydantic's use
-   [database.py](lms_proj/database.py) - To configure the database
-   [crud.py](lms_proj/crud.py) - Handles the CRUD operations

---
## APIs:

-   POST  - `/book/`
    ```json
    {
        "title": "string"
    }
    ```

-   POST - `/inventory/`
    ```json
    {
        "title": "string",
        "stock": 0
    }
    ```

-   POST - `/student/`
    ```json
    {
        rollNo: 0
    }
    ```

-   POST - `/issue/`
    ```json
    {
        "title": "string",
        "issuedBy": 0
    }
    ```

-   DELETE - `/return/`
    ```json
    {
        "title": "string",
        "issuedBy": 0
    }
    ```

-   GET `/popular/`

Note: http://127.0.0.1:8000/docs for trying out the API

---
## Built With
- [Python](www.google.com)
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework for building API
- [SQLAlchemy](https://www.sqlalchemy.org/) - MySQL ORM for Python
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
- [Poetry](https://python-poetry.org/) - Dependency management and packagin in python