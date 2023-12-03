from sqlalchemy import Column, Integer, TEXT, DATE, Boolean, VARCHAR

from .base import BaseModel


class Fact(BaseModel):
    __tablename__ = 'Facts'

    level_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    base_fact = Column(VARCHAR, unique=True, nullable=False)
    fact_1 = Column(VARCHAR, unique=True, nullable=False)
    fact_2 = Column(VARCHAR, unique=True, nullable=False)
    fact_3 = Column(VARCHAR, unique=True, nullable=False)
    fact_4 = Column(VARCHAR, unique=True, nullable=False)
    fact_5 = Column(VARCHAR, unique=True, nullable=False)
    fact_6 = Column(VARCHAR, unique=True, nullable=False)
    fact_7 = Column(VARCHAR, unique=True, nullable=False)
    fact_8 = Column(VARCHAR, unique=True, nullable=False)
    fact_9 = Column(VARCHAR, unique=True, nullable=False)
    fact_10 = Column(VARCHAR, unique=True, nullable=False)

    def __str__(self) -> str:
        return f"<User:{self.level_id}>"

