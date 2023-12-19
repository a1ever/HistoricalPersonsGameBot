from sqlalchemy import Column, Integer, VARCHAR

from .base import BaseModel


class General(BaseModel):
    __tablename__ = 'General'

    level_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    full_name = Column(VARCHAR(200), nullable=False)
    country = Column(VARCHAR(200), nullable=False)
    date_of_birth = Column(VARCHAR(200), nullable=False)
    date_of_death = Column(VARCHAR(200), nullable=False)
    link_to_photo = Column(VARCHAR(200), nullable=False)
    activity = Column(VARCHAR(200), nullable=False)

    def __str__(self) -> str:
        return f"<User:{self.level_id}>"

    def get_age_fact(self, amount: int) -> str:
        ans = ""
        if amount >= 2:
            ans += "Родился: " + self.date_of_birth + "\n"
        if amount >= 1:
            ans += "Умер: " + self.date_of_death + "\n"
        return ans
