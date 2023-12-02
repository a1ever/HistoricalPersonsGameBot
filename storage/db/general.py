from sqlalchemy import Column, Integer, VARCHAR, DATE, Boolean
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

    def __str__(self) -> str:
        return f"<User:{self.level_id}>"

