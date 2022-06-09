from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'mysql://root:password@localhost/lms'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
create_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()