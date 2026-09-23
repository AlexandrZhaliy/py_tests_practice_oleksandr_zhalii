# this module describes the table structure in which the data will be added
# tables creation is executed within db_tables_creation (see db_connect.init_db)

from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Result(Base):
    """
    Represents one result produced by the application and persisted
    to PostgreSQL (homework requirement #1: app saves its result to the DB).
    """
    __tablename__ = "results"

    id = Column(Integer, primary_key=True)
    task_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Result id={self.id} task_name={self.task_name!r} value={self.value}>"
