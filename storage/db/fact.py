from sqlalchemy import Column, Integer, VARCHAR

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
    fact_10 = Column(VARCHAR, unique=True, nullable=True)

    def __str__(self) -> str:
        return f"<User:{self.level_id}>"

    def get_facts(self, amount: int) -> str:
        ans = "Факты: \n" + self.base_fact + "\n"
        if amount >= 10:
            ans += self.fact_10 + "\n" + "\n"
        if amount >= 9:
            ans += self.fact_9 + "\n" + "\n"
        if amount >= 8:
            ans += self.fact_8 + "\n" + "\n"
        if amount >= 7:
            ans += self.fact_7 + "\n" + "\n"
        if amount >= 6:
            ans += self.fact_6 + "\n" + "\n"
        if amount >= 5:
            ans += self.fact_5 + "\n" + "\n"
        if amount >= 4:
            ans += self.fact_4 + "\n" + "\n"
        if amount >= 3:
            ans += self.fact_3 + "\n" + "\n"
        if amount >= 2:
            ans += self.fact_2 + "\n" + "\n"
        if amount >= 1:
            ans += self.fact_1 + "\n" + "\n" + "\n"
        return ans