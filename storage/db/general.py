from sqlalchemy import Column, Integer, VARCHAR, DATE
from sqlalchemy.orm import relationship

from .base import BaseModel


class General(BaseModel):
    __tablename__ = 'General'

    level_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    full_name = Column(VARCHAR, nullable=False)
    country = Column(VARCHAR, nullable=False)
    date_of_birth = Column(DATE, nullable=False)
    date_of_death = Column(DATE, nullable=False)
    link_to_photo = Column(VARCHAR, nullable=False)
    activity = Column(VARCHAR, nullable=False)

    quotes = relationship("Quotes", back_populates="General")
    facts = relationship("Facts", back_populates="General")

    def __str__(self) -> str:
        return f"<User:{self.level_id}>"
