from sqlalchemy import Column, Integer, VARCHAR, DATE, Boolean
from .base import BaseModel

class User(BaseModel):
    __tablename__ = 'Users'

    # Telegram user id
    uuid = Column(Integer, unique=True, nullable=False)

    # Telegram user name
    username = Column(VARCHAR(32), unique=False, nullable=True, primary_key=True)
    campaign_status = Column(Integer, unique=False, nullable=True)
    random_problem = Column(Integer, unique=False, nullable=True)
    is_in_campaign = Column(Boolean, unique=False, nullable=False)
    campaign_score = Column(Integer, unique=False, default=0)
    random_problems_score = Column(Integer, unique=False, default=0)

    # reg_date = Column(DATE, default=datetime.date.today())
    # upd_date = Column(DATE, onupdate=datetime.date.today())

    def __str__(self) -> str:
        return f"<User:{self.uuid}>"

