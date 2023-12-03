from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class Quote(BaseModel):
    __tablename__ = 'Quotes'

    level_id = Column(Integer, ForeignKey("General.level_id"), unique=True, nullable=False, primary_key=True)
    quote_1 = Column(VARCHAR, unique=True, nullable=False)
    quote_2 = Column(VARCHAR, unique=True, nullable=False)
    quote_3 = Column(VARCHAR, unique=True, nullable=False)
    quote_4 = Column(VARCHAR, unique=True, nullable=False)
    quote_5 = Column(VARCHAR, unique=True, nullable=False)

    general = relationship("General", back_populates="Quotes")

    def __str__(self) -> str:
        return f"<User:{self.level_id}>"
