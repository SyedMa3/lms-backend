# Library Management - Backend

## To run the application:

-   You need to have [Poetry](https://python-poetry.org/) installed on your system

-   ```bash
    poetry install
    ```

- The application currently uses MySQL. You can configure the database connection in `database.py` using `SQLALCHEMY_DATABASE_URL`

- Make sure you have created a database you mentioned above

-   ```bash
    poetry run uvicorn lms_proj.main:app --reload
     ```
    Run this command to start the server. 
    ```
    --reload is not used in production
    ```


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


## Structure of Application:

-   `main.py` - Deals with routing,
-   `models.py` - To declare classes to create tables from ORM
-   `schemas.py` - Schemas of the models for Pydantic's use
-   `database.py` - To configure the database
-   `crud.py` - Does all the operations given in PDF