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
    -   id
    -   title
    -   timesIssued
    -   inv_id

- Inventory: (To store the inventory of available books)
    -   id
    -   title
    -   stock

- Student: (To store the students added)
    -   rollNo
    -   booksIssued

- Issue: (To store the currently issued books)
    -   id
    -   title
    -   book_id
    -   issuedBy
    