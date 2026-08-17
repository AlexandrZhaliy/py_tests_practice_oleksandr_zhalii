# this module makes connection to database
# tables creation will be executed within db_tables_creation.py module
# data filling will be executed within db_data_filling.py module

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    print("Database connection successful!")

Session = sessionmaker(bind=engine)
session = Session()