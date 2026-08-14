# this module creates tables in database using models.py tables model
# before the current module execution db connection should be successfully established via db_connect.py module
# data filling will be executed within db_data_filling.py module

from db_connect import engine
from models import Base


Base.metadata.create_all(engine)
print("Tables created successfully!")