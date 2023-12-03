from sqlalchemy import select

from storage.FactState import Fact
from storage.db import General, Fact, Quote

# s = (select()
#      .select_from(General
#                   .join(Fact, General.level_id == Fact.level_id)
#                   .join(Quote, General.level_id == Quote.level_id))
#      )


async def get_personal_info(user_id: int):
    return f"Ты хорош, {user_id}, а статистика в бд)"


async def get_top_info(user_id: int) -> object:
    return f"Ты хорош, {user_id}, а статистика в бд)"


async def get_surrender(user_id: int):
    return f"Слабый"


async def get_current_fact_state(user_id: int):
    return Fact
