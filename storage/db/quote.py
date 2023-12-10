from sqlalchemy import Column, Integer, VARCHAR

from .base import BaseModel


class Quote(BaseModel):
    __tablename__ = 'Quotes'

    level_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    quote_1 = Column(VARCHAR, nullable=False)
    quote_2 = Column(VARCHAR, nullable=False)
    quote_3 = Column(VARCHAR, nullable=False)
    quote_4 = Column(VARCHAR, nullable=False)
    quote_5 = Column(VARCHAR, nullable=False)

    def __str__(self) -> str:
        return f"<User:{self.level_id}>"

    def get_quotes(self, amount: int) -> str:
        ans = ""
        if amount == 5:
            ans += self.quote_5 + "\n" + "\n"
        if amount >= 4:
            ans += self.quote_4 + "\n" + "\n"
        if amount >= 3:
            ans += self.quote_3 + "\n" + "\n"
        if amount >= 2:
            ans += self.quote_2 + "\n" + "\n"
        if amount >= 1:
            ans = "Цитаты:\n" + ans + self.quote_1 + "\n" + "\n"
        return ans
