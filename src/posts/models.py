from sqlalchemy import Column, Integer, String
from src.database import Base

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False) 