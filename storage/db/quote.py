from sqlalchemy import Column, Integer, VARCHAR

from .base import BaseModel


class Quote(BaseModel):
    __tablename__ = 'Quotes'

    level_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    quote_1 = Column(VARCHAR(200), nullable=False)
    quote_2 = Column(VARCHAR(200), nullable=False)
    quote_3 = Column(VARCHAR(200), nullable=False)
    quote_4 = Column(VARCHAR(200), nullable=False)
    quote_5 = Column(VARCHAR(200), nullable=False)

    def __str__(self) -> str:
        return f"<User:{self.level_id}>"

    def get_quotes(self, amount: int, quote_order: str) -> str:
        quotes = [self.quote_1, self.quote_2, self.quote_3, self.quote_4, self.quote_5]
        arr = [quotes[int(i)] for i in quote_order.split()]
        return "\n".join(f'Цитата {i+1}: "{qt}"\n' for i, qt in enumerate(arr[0:amount])) + "\n"
