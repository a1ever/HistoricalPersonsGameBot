from sqlalchemy import Column, Integer, VARCHAR, DATE, Boolean
from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'Quotes'

    level_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    quote_1 = Column(VARCHAR,  unique=True, nullable=False)
    quote_2 = Column(VARCHAR, unique=True, nullable=False)
    quote_3 = Column(VARCHAR, unique=True, nullable=False)
    quote_4 = Column(VARCHAR, unique=True, nullable=False)
    quote_5 = Column(VARCHAR, unique=True, nullable=False)
    def __str__(self) -> str:
        return f"<User:{self.level_id}>"

