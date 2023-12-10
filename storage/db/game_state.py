from sqlalchemy import Column, Integer, Boolean, UniqueConstraint

from .base import BaseModel


class GameState(BaseModel):
    __tablename__ = 'Game_states'

    uuid = Column(Integer, nullable=False, primary_key=True)
    type_of_game = Column(Boolean, nullable=False, primary_key=True)
    level_id = Column(Integer, nullable=False)
    fact_amount = Column(Integer, default=0)
    age_fact_amount = Column(Integer, default=0)
    displayed_country = Column(Boolean, default=False)
    displayed_photo = Column(Boolean, default=False)
    displayed_activity = Column(Boolean, default=False)
    quote_amount = Column(Integer, default=0)
    minus_points = Column(Integer, default=0)
    UniqueConstraint("uuid", "type_of_game", name="uix_1")

    def __str__(self) -> str:
        return f">"

    def withNewFactAmount(self, val: int):
        self.fact_amount = val
        return self

    def withNewAgeFactAmount(self, val: int):
        self.age_fact_amount = val
        return self

    def withNewQuoteAmount(self, val: int):
        self.quote_amount = val
        return self

    def addMinus(self, val: int):
        self.minus_points += val
        return self

    def withDisplayedCountry(self):
        self.displayed_country = True
        return self

    def withDisplayedPhoto(self):
        self.displayed_photo = True
        return self


    def withDisplayedActivity(self):
        self.displayed_activity = True
        return self
