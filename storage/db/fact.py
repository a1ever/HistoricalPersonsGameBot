from sqlalchemy import Column, Integer, TEXT, DATE

from .base import BaseModel


class Fact(BaseModel):
    __tablename__ = 'users'

    uuid = Column(Integer, unique=True, nullable=False, primary_key=True)
    level_id = Column(Integer, unique=True, nullable=False)

    def __str__(self) -> str:
        print("aboba")