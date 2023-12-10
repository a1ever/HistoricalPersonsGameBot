class GameStateModel:
    uuid: int
    level_id: int
    type_of_game: bool
    fact_amount: int
    age_fact_amount: int
    displayed_country: int
    displayed_photo: int
    displayed_activity: int
    quote_amount: int
    minus_points: int

    def __str__(self) -> str:
        return f""

    def addFactAmount(self):
        self.fact_amount += 1
        return self

    def addAgeFactAmount(self):
        self.age_fact_amount += 1
        return self

    def addQuoteAmount(self):
        self.quote_amount += 1
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

    def is_done(self) -> bool:
        return self.quote_amount == 5 and self.fact_amount == 11 and self.age_fact_amount == 2 and \
               self.displayed_country and self.displayed_photo and self.displayed_activity
