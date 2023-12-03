from sqlalchemy import Column, VARCHAR
from .base import BaseModel


class EasterEgg(BaseModel):
    __tablename__ = 'Easter_eggs'

    frase = Column(VARCHAR, unique=True, nullable=False, primary_key=True)
    result = Column(VARCHAR, nullable=False)

    def __str__(self) -> str:
        return f"<User:{self.level_id}>"

