from sqlalchemy import Column, VARCHAR
from .base import BaseModel


class EasterEgg(BaseModel):
    __tablename__ = 'Easter_eggs'

    frase = Column(VARCHAR(1), unique=True, nullable=False, primary_key=True)
    result = Column(VARCHAR(1), nullable=False)

    def __str__(self) -> str:
        return f"<User:{self.level_id}>"

