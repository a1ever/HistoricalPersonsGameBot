from sqlalchemy import Column, Integer, VARCHAR

from .base import BaseModel


class Fact(BaseModel):
    __tablename__ = 'Facts'

    level_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    base_fact = Column(VARCHAR(200), unique=True, nullable=False)
    fact_1 = Column(VARCHAR(200), unique=True, nullable=False)
    fact_2 = Column(VARCHAR(200), unique=True, nullable=False)
    fact_3 = Column(VARCHAR(200), unique=True, nullable=False)
    fact_4 = Column(VARCHAR(200), unique=True, nullable=False)
    fact_5 = Column(VARCHAR(200), unique=True, nullable=False)
    fact_6 = Column(VARCHAR(200), unique=True, nullable=False)
    fact_7 = Column(VARCHAR(200), unique=True, nullable=False)
    fact_8 = Column(VARCHAR(200), unique=True, nullable=False)
    fact_9 = Column(VARCHAR(200), unique=True, nullable=False)
    fact_10 = Column(VARCHAR(200), unique=True, nullable=True)

    def __str__(self) -> str:
        return f"<User:{self.level_id}>"

    def get_facts(self, amount: int, fact_order: str) -> str:
        facts = [self.base_fact, self.fact_1, self.fact_2, self.fact_3, self.fact_4, self.fact_5, self.fact_6, self.fact_7, self.fact_8, self.fact_9, self.fact_10]
        arr = [facts[int(i)] for i in fact_order.split()]
        return "\n".join(f"Факт {i + 1}: {qt}\n" for i, qt in enumerate(arr[0:amount])) + "\n"