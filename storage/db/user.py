from sqlalchemy import Column, Integer, VARCHAR, Boolean
from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'Users'

    # Telegram user id
    uuid = Column(Integer, unique=True, nullable=False, primary_key=True)

    # Telegram user name
    username = Column(VARCHAR(32), unique=False, nullable=True)
    campaign_status = Column(Integer, unique=False, nullable=True, default=1)
    is_in_campaign = Column(Boolean, unique=False, nullable=False, default=False)
    campaign_score = Column(Integer, unique=False, default=0)
    random_problems_score = Column(Integer, unique=False, default=0)

    def __str__(self) -> str:
        return f"<User:{self.uuid}>"
