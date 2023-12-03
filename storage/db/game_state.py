from sqlalchemy import Column, Integer, Boolean

from .base import BaseModel


class GameState(BaseModel):
    __tablename__ = 'Game_states'

    uuid = Column(Integer, unique=True, nullable=False, primary_key=True)
    level_id = Column(Integer, unique=False, nullable=False)
    fact_amount = Column(Integer, default=0)
    age_fact_amount = Column(Integer, default=0)
    displayed_country = Column(Boolean, default=False)
    displayed_photo = Column(Boolean, default=False)
    displayed_activity = Column(Boolean, default=False)
    quote_amount = Column(Integer, default=0)
    minus_points = Column(Integer, default=0)

    def __str__(self) -> str:
        return f"<User:{self.uuid, "  ", self.minus_points}>"

