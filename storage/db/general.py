from sqlalchemy import Column, Integer, VARCHAR

from .base import BaseModel


class General(BaseModel):
    __tablename__ = 'General'

    level_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    full_name = Column(VARCHAR, nullable=False)
    country = Column(VARCHAR, nullable=False)
    date_of_birth = Column(VARCHAR, nullable=False)
    date_of_death = Column(VARCHAR, nullable=False)
    link_to_photo = Column(VARCHAR, nullable=False)
    activity = Column(VARCHAR, nullable=False)

    def __str__(self) -> str:
        return f"<User:{self.level_id}>"

    def get_age_fact(self, amount: int) -> str:
        ans = ""
        if amount >= 2:
            ans += "Родился: " + self.date_of_birth + "\n"
        if amount >= 1:
            ans += "Умер: " + self.date_of_death + "\n"
        return ans
