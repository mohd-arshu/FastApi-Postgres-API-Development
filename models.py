from database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String
from sqlalchemy.sql.expression import text
# from pydantic import EmailStr

class SampleEcom(Base):
    __tablename__ = "sample_ecom"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    ratings = Column(Integer, index=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))