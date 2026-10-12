from database import Base
from sqlalchemy import Column, Integer, String

class SampleEcom(Base):
    __tablename__ = "sample_ecom"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    ratings = Column(Integer, index=True)