from storage.Models.fact_model import FactModel


class Fact:
    fact_itself: FactModel
    level_id: int
    age_fact_amount: int
    max_age_fact_amount = 3
    fact_amount: int
    max_fact_amount: int
    quote_amount: int
    max_quote_amount: int
    displayed_country: bool
    displayed_photo: bool
    displayed_activity: bool
    minus_points: int
